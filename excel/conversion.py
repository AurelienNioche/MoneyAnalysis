# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import xlsxwriter
from tqdm import tqdm

from game.models import Room, User, Choice


def write_worksheet(workbook, data, worksheet_name):
    """
    Write table data to excel workbook (add a worksheet)
    :param data: the content of the worksheet
    :param workbook: the workbook (excel file)
    :param worksheet_name: the worksheet name
    :return: the workbook with worksheet added
    """

    worksheet = workbook.add_worksheet(worksheet_name)

    # prepare column title format
    title = workbook.add_format({'bold': True})
    title.set_bottom()

    # prepare data format (alignment)
    align = workbook.add_format()
    align.set_align("left")

    rows = data
    cols = range(len(data[0]))

    # fit column size to content
    for col_number in cols:
        max_width = \
            max(len(str(rows[j][col_number])) for j in range(len(rows)))

        worksheet.set_column(col_number, col_number, max_width)

    # Iterate over the data and write it out row by row
    # Format column title if row == 0
    for row_number, row in enumerate(rows):
        for col_number in cols:

            if row_number == 0:
                worksheet.write(row_number, col_number, row[col_number], title)
            else:
                worksheet.write(row_number, col_number, row[col_number], align)


def get_formatted_data():

    label = {
        414: "3_good_non_uniform",
        415: "4_good_uniform",
        416: "3_good_uniform",
        417: "4_good_non_uniform"
    }

    good_map = {
        3: {
            0: 0,
            1: 2,
            2: 1
        },
        4: {
            0: 0,
            1: 3,
            2: 2,
            3: 1
        }
    }

    cols = (
        "room_id",
        "n_good",
        "uniform_repartition",
        "user_id",
        "prod",
        "cons",
        "t",
        "in_hand",
        "desired",
        "success"
    )

    data = {}

    rooms = Room.objects.filter(state="end").order_by("id")

    for r in tqdm(rooms):

        data_sheet = [cols, ]

        n_good = r.n_type

        equal_repartition = int('non_uniform' not in label[r.id])

        users = User.objects.filter(room_id=r.id)

        for t in range(r.t_max):

            for u in users:

                c = Choice.objects.get(user_id=u.id, t=t)

                row = [
                    r.id, n_good, equal_repartition,
                    u.id,
                    good_map[n_good][u.production_good],
                    good_map[n_good][u.consumption_good],
                    t,
                    good_map[n_good][c.good_in_hand],
                    good_map[n_good][c.desired_good],
                    int(c.success)
                ]

                data_sheet.append(row)

        data[label[r.id]] = data_sheet

    return data


def run():
    save_path = "data/excel_data.xlsx"
    os.makedirs('data', exist_ok=True)
    workbook = xlsxwriter.Workbook(save_path)

    data = get_formatted_data()

    for k, v in data.items():
        write_worksheet(
            workbook=workbook, data=v,
            worksheet_name=k)

    workbook.close()


if __name__ == '__main__':
    run()
