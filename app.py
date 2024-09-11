from fileinput import close

import flet as ft

def main(pagina: ft.Page):
    pagina.title="App Flet"
    pagina.vertical_alignment=ft.MainAxisAlignment.CENTER

    def abrir(e):

        def crip(e):
            pagina.clean()
            m = ' '
            for i in valor:
                m = m + chr(ord(i)+8)

            msg2 = ft.Text('Mensagem criptografada:')
            msg3 = ft.Text(m)
            volta1 = ft.TextButton("Voltar", on_click=voltar)
            pagina.add(ft.Row([msg2,msg3], alignment=ft.MainAxisAlignment.CENTER))
            pagina.add(ft.Row([volta1], alignment=ft.MainAxisAlignment.CENTER))

        def descrip(e):
            pagina.clean()
            m = ' '
            for i in valor:
                m = m + chr(ord(i) - 8)

            msg2 = ft.Text('Mensagem descriptografada:')
            msg3 = ft.Text(m)
            volta2 = ft.TextButton("Voltar", on_click=voltar)
            pagina.add(ft.Row([msg2, msg3], alignment=ft.MainAxisAlignment.CENTER))
            pagina.add(ft.Row([volta2], alignment=ft.MainAxisAlignment.CENTER))

        def voltar(e):
            pagina.clean()
            main(pagina)

        try:
            arquivo = open(texto.value,"r")
            valor = arquivo.read()
            msg = ft.Text("O arquivo "+texto.value + " foi aberto!!!")
            msg1 = ft.Text("Conteudo do arquivo:")
            conteudo = ft.Text(valor)
            bot1 = ft.TextButton("Criptografar", on_click=crip)
            bot2 = ft.TextButton("Descriptografar", on_click=descrip)
            pagina.clean()
            pagina.add(ft.Row([msg], alignment=ft.MainAxisAlignment.CENTER))
            pagina.add(ft.Row([msg1,conteudo], alignment=ft.MainAxisAlignment.CENTER))
            pagina.add(ft.Row([bot1, bot2], alignment=ft.MainAxisAlignment.CENTER))
        except:
            pagina.clean()
            erro =  ft.Text("Não existe este arquivo", text_align=ft.TextAlign.CENTER)
            volta = ft.TextButton("Voltar", on_click=voltar)
            pagina.add(ft.Row([erro], alignment=ft.MainAxisAlignment.CENTER))
            pagina.add(ft.Row([volta], alignment=ft.MainAxisAlignment.CENTER))

    #o que eu quero
    texto = ft.TextField()
    pergunta =  ft.Text("Digite o nome do arquivo com extensão", text_align=ft.TextAlign.CENTER)
    botao = ft.TextButton("Abrir o arquivo",on_click = abrir)
    pagina.add(ft.Row([pergunta],alignment=ft.MainAxisAlignment.CENTER))
    pagina.add(ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER))
    pagina.add(ft.Row([botao], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main)