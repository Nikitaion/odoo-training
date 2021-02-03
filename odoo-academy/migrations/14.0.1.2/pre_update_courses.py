def migrate(cr, version):
    table_name, column_name = 'academy_course', 'name'

    query = """" DELETE
    FROM academy_course a
    WHERE a.name <> (SELECT min(b.name)
    FROM academy_course b
    WHERE a.key = b.key);
    """


    cr.execute(query)

    # DELETE
    # FROM
    # academy_course
    # WHERE
    # academy_course.name = academy_course.name;
