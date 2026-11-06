from django.db import migrations, models


def add_optional_fields_to_legacy_table(apps, schema_editor):
    connection = schema_editor.connection
    table_name = "clientes"
    if table_name not in connection.introspection.table_names():
        return

    existing_columns = {
        column.name
        for column in connection.introspection.get_table_description(
            schema_editor.connection.cursor(),
            table_name,
        )
    }
    fields = (
        ("edad", models.PositiveSmallIntegerField(blank=True, null=True)),
        (
            "peso",
            models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
            ),
        ),
    )
    for name, field in fields:
        if name not in existing_columns:
            column_type = field.db_type(connection)
            schema_editor.execute(
                f"ALTER TABLE {schema_editor.quote_name(table_name)} "
                f"ADD COLUMN {schema_editor.quote_name(name)} {column_type} NULL"
            )


def remove_optional_fields_from_legacy_table(apps, schema_editor):
    connection = schema_editor.connection
    table_name = "clientes"
    if table_name not in connection.introspection.table_names():
        return

    existing_columns = {
        column.name
        for column in connection.introspection.get_table_description(
            schema_editor.connection.cursor(),
            table_name,
        )
    }
    for name in ("peso", "edad"):
        if name in existing_columns:
            schema_editor.execute(
                f"ALTER TABLE {schema_editor.quote_name(table_name)} "
                f"DROP COLUMN {schema_editor.quote_name(name)}"
            )


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ("apps", "0002_remove_cita_id_cita_enlace_virtual_cita_id_cita_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="edad",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="peso",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
            ),
        ),
        migrations.RunPython(
            add_optional_fields_to_legacy_table,
            remove_optional_fields_from_legacy_table,
        ),
    ]
