import psycopg2


def read_db(product_id, track_order):
    try:
        connection = psycopg2.connect(
                                      host = '127.0.0.1',
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
