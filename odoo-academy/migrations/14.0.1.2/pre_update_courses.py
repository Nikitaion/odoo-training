def migrate(cr, version):
    table_name, column_name = 'academy_course', 'name'

    query = """" DELETE FROM academy_course a
    WHERE a.id <> (SELECT min(b.id)
    FROM academy_course b
    WHERE a.name = b.name);
    """


    cr.execute(query)

    # DELETE
    # FROM
    # academy_course
    # WHERE
    # academy_course.name = academy_course.name;
