def migrate(cr, version):
    table_name, column_name = 'academy_course', 'name'

    query = """" DELETE FROM
    academy_course x
    USING academy_course y
    WHERE
    x.name = y.name;
    """


