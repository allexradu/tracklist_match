import psycopg2


def read_db(product_id, track_order):
    try:
        connection = psycopg2.connect(database = 'tracklist', user = 'allex', password = '',
                                      host = '207.180.212.129',
                                      port = '5432')
    except psycopg2.Error as err:
        print('An error occurred while trying to connect to the database')
    else:
        print('Connection to the database was successful!')

        cursor = connection.cursor()

        cursor.execute(f"""
            select link_sample, cd, track_order, song_title, artists, duration 
            from 
            test.track_list where product_id='{product_id}' and track_order='{track_order}';
        """)

        record = cursor.fetchone()

        if record is not None:
            print('record found: ', record)
            return record

        else:
            print('record not found')
            return None


def update_local_server(product_code, product_id, table_string):
    try:
        connection2 = psycopg2.connect(database = 'tracklist', user = 'allex', password = '',
                                       host = '207.180.212.129',
                                       port = '5432')
    except psycopg2.Error as err:
        print('An error occurred while trying to connect to the database')
    else:
        print('Connection to the database was successful!')

        def sanitize_single_line_string(initial_string):
            string = str(initial_string)
            if string is not None:
                return string.replace("'", "''") if string.find(
                    "'") != -1 else string
            else:
                return string

        cursor = connection2.cursor()
        cursor.execute(f"""
                            insert into test.import_table(product_code, product_id, description) 
                            values (
                            '{product_code}',
                            '{product_id}',
                            '{sanitize_single_line_string(table_string)}'
                            );
                        """)
        connection2.commit()
        connection2.close()
