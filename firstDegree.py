import flet as ft


def first(page: ft.Page):

   # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.auto_scroll = True
    page.scroll = ft.ScrollMode.HIDDEN

    page.adaptive = True
    page.bgcolor = "white"

    page.appbar = ft.AppBar( 
        leading_width=50,
        center_title=False,
        bgcolor= "#556ad0",
       
    )

    page.drawer = ft.NavigationDrawer(
            bgcolor= "#556ad0",
            controls=[
            ft.Container(
                height=12),
            ft.Container(
                content = ft.Text(
                "Fast Operation",
                weight = ft.FontWeight.BOLD,
                size = 15
            ),
            padding = 20
            
            )
            ,
            ft.Divider(thickness=2),
            

            ft.ExpansionTile(
            title=ft.Text("Equazioni"),
            affinity=ft.TileAffinity.PLATFORM,
            maintain_state=False,
            collapsed_text_color=ft.colors.WHITE,
            text_color=ft.colors.WHITE,
            controls=[ft.ListTile(title=ft.TextButton("Primo Grado", data=0))],
            bgcolor="#556ad0",
        ),


        ft.ExpansionTile(
            title=ft.Text("Disequazioni"),
            affinity=ft.TileAffinity.PLATFORM,
            maintain_state=True,
            collapsed_text_color=ft.colors.WHITE,
            text_color=ft.colors.WHITE,
            controls=[ft.ListTile(title=ft.TextButton("Primo Grado")), ft.ListTile(title=ft.TextButton("Secondo Grado"))],
            bgcolor="#556ad0"
        ),


        ],
    )

    page.add(
        ft.SafeArea( 
            ft.Column(
                [
                    ft.Text("Equazioni di PRIMO GRADO")
                ]
            )
        ),
       page.appbar
    )
