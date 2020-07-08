import excel
import read_db

product_id_column = 'B'
description_column = 'C'

excel.get_track_list_table(product_id_column)

print('excel read')

track_order = 1
table_string = ''

for i in range(1, len(excel.product_ids)):
    print(f'Processing {i} / {len(excel.product_ids)} : {excel.product_ids[i]}')
    track_order = 1
    while True:
        print(f'getting product_id {excel.product_ids[i]} track_order: {track_order}')
        record = read_db.read_db(excel.product_ids[i], track_order)

        if record is not None:

            if track_order == 1:
                table_string = \
                    f"""
                    <table style="hdz-track-list">
                        <tr>
                            <th class="hdz-track-list__th">MP3</th>
                            <th class="hdz-track-list__th">Disc</th>
                            <th class="hdz-track-list__th">Track</th>
                            <th class="hdz-track-list__th">Titlu</th>
                            <th class="hdz-track-list__th">Artist</th>
                            <th class="hdz-track-list__th">Durata</th>
                        </th>
                        <tr>
                            <td class="hdz-track-list__td"><a href="{record[0]}" class="hdz-track-list__play">Play</a></td>
                            <td class="hdz-track-list__td">{record[1]}</td>
                            <td class="hdz-track-list__td">{record[2]}</td>
                            <td class="hdz-track-list__td">{record[3]}</td>
                            <td class="hdz-track-list__td">{record[4]}</td>
                            <td class="hdz-track-list__td">{record[5]}</td>
                        </tr>
                    """
                track_order += 1
            else:
                f"""
                    <table style="width:100%">
                        <tr>
                            <td class="hdz-track-list__td"><a href="{record[0]}" class="hdz-track-list__play">Play</a></td>
                            <td class="hdz-track-list__td">{record[1]}</td>
                            <td class="hdz-track-list__td">{record[2]}</td>
                            <td class="hdz-track-list__td">{record[3]}</td>
                            <td class="hdz-track-list__td">{record[4]}</td>
                            <td class="hdz-track-list__td">{record[5]}</td>
                        </tr>
                """
                track_order += 1
        else:
            if track_order == 1:

                break
            else:
                table_string += \
                    f"""
                    </table>
                    """
                excel.write_description_to_excel(table_string, description_column)
                excel.work_sheet_index += 1
                table_string = ''
                track_order = 1
                break
