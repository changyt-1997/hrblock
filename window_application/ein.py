import time
import random

import flet as ft
from flet import Page
import pandas as pd

from core.zip_info import get_zip_info, get_ein_info


class Ein(object):
    def __init__(self, page: ft.Page):
        self.page = page
        self.data = None
        self.file_data = None
        self.download_data = None
        self.main()

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        try:
            self.page.controls.pop()
        except:
            pass
        if e.files is None:
            return
        data_file = e.files[0]
        df = pd.read_excel(data_file.path)
        self.file_data = df
        try:
            self.data = df["邮编"].to_list()
        except Exception as e:
            self.page.add(ft.Text(f"读取文件失败 {e}"))
            return

        self.page.add(ft.Text("已读取文件", style="headlineSmall"))

    def start_search(self, e):
        print("start_search")
        self.page.controls.pop()
        pb = ft.ProgressBar(width=400)
        card = ft.Card(height=500)
        cols = ft.Column([
            ft.Text("正在查找", style="headlineSmall"),
            ft.Column([ft.Text("Doing something..."), pb]),
            ft.Text("检索中", style="headlineSmall"),
            ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee"),
        ])
        card.content = ft.Container(width=500, content=cols, padding=ft.padding.symmetric(vertical=10))
        self.page.add(card)
        data_result = []
        for i, v in enumerate(self.data):
            pb.value = i / len(self.data)
            pb.label = f"{i} / {len(self.data)}"
            self.page.update()
            if len(str(v)) == 4:
                v = f"0{str(v)}"
            try:
                try:
                    index = random.randint(1, 15)
                    emp_name, emp_number, emp_address, emp_address_zip = get_zip_info(v, index)
                except:
                    emp_name, emp_number, emp_address, emp_address_zip = None, None, None, None
                if not emp_name:
                    index = random.randint(1, 30)
                    try:
                        emp_name, emp_number, emp_address = get_ein_info(v, index)
                    except:
                        index = random.randint(1, 30)
                        emp_name, emp_number, emp_address = get_ein_info(v, index)
                data_result.append({"邮编": v, "公司名称": emp_name, "公司编号": emp_number, "公司地址": emp_address})
            except Exception as e:
                data_result.append({"邮编": v, "公司名称": None, "公司编号": None, "公司地址": None})
        self.page.controls.pop()
        df = pd.DataFrame(data_result)
        self.download_data = df.drop('邮编', axis=1)
        col_list = df.columns.to_list()
        columns = []
        for i in col_list:
            columns.append(ft.DataColumn(ft.Text(i)))
        rows = []
        data = df.iloc[1:].to_dict(orient='index')
        for i in data:
            cells = []
            for j in col_list:
                cell = ft.DataCell(ft.Text(data[i][j]))
                cells.append(cell)
            rows.append(ft.DataRow(cells))
        table = ft.DataTable(
            columns=columns,
            rows=rows,
        )
        self.page.add(table)
        self.page.update()

    def download_file(self, e):
        result = pd.concat([self.file_data, self.download_data], axis=1)
        result.to_excel("搜索结果.xlsx", index=False)
        self.page.snack_bar.open = True

    def main(self):
        self.page.title = 'ein查询'
        self.page.auto_scroll = True
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        pick_file = ft.FilePicker(on_result=self.pick_files_result)
        self.page.overlay.append(pick_file)
        self.page.appbar = ft.AppBar(
            leading_width=40,
            title=ft.Text("EIN 查询"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(
                    ft.icons.FILE_OPEN,
                    on_click=lambda _: pick_file.pick_files(allow_multiple=False, allowed_extensions=['xlsx'])
                ),
                ft.IconButton(ft.icons.FILE_DOWNLOAD, on_click=self.download_file),
                ft.IconButton(ft.icons.NOT_STARTED, on_click=self.start_search),
                # ft.IconButton(ft.icons.PAUSE_CIRCLE),
            ],
        )
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("已保存至当前目录下！！！"),
            action="Alright!",
        )
        self.page.update()


if __name__ == '__main__':
    ft.app(Ein)