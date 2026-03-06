# -*- coding: utf-8 -*-

def formatar_texto(texto):
    """
    Formata o corpo do texto transformando linhas curtas ou marcadas com # em H2 
    e o restante em parágrafos justificados.
    """
    linhas = [l.strip() for l in texto.split("\n") if l.strip()]
    html_final = ""
    COR_MD = "rgb(7, 55, 99)"
    
    for linha in linhas:
        e_titulo = linha.startswith("#")
        linha_limpa = linha.strip("#* ").strip()

        # Ordem 5: Subtítulo H2 - Arial 20, Bold, Esquerda, Cor MD + Maiúsculas
        if e_titulo or (len(linha_limpa.split()) <= 18 and not linha_limpa.endswith(".")):
            html_final += f"""
            <h2 style="text-align:left !important; font-family:Arial !important; color:{COR_MD} !important; 
                       font-size:20px !important; font-weight:bold !important; text-transform:uppercase !important; 
                       margin-top:25px !important;">
                {linha_limpa}
            </h2>
            """
        else:
            # Ordem 6: Texto - Fonte 18, Justificado, Cor MD
            html_final += f"""
            <p style="text-align:justify !important; font-family:Arial !important; color:{COR_MD} !important; 
                      font-size:18px !important; line-height:1.6 !important; margin-bottom:15px !important;">
                {linha_limpa}
            </p>
            """
    return html_final

def obter_esqueleto_html(dados):
    """
    Monta a estrutura principal do post buscando dados de funções externas.
    """
    # Ordens 1, 3 e 7: Busca de dados externos
    titulo = dados.get("titulo", "")
    imagem = dados.get("imagem", "")
    texto_completo = dados.get("texto_completo", "")
    assinatura = dados.get("assinatura", "")

    conteudo_formatado = formatar_texto(texto_completo)

    html = f"""
<div style="max-width:900px !important; margin:auto !important; font-family:Arial, sans-serif !important;">

    <h3 style="text-align:center !important; font-family:Arial !important; font-size:28px !important; 
               font-weight:bold !important; color:rgb(7, 55, 99) !important; text-transform:uppercase !important; 
               margin-bottom:20px !important;">
        {titulo}
    </h3>

    <div style="text-align:center !important; margin-bottom:25px !important;">
        <img src="{imagem}" style="width:100% !important; height:auto !important; display:block !important; margin:auto !important;">
    </div>

    <div>
        {conteudo_formatado}
    </div>

    <div style="margin-top:40px !important; padding-top:20px !important; border-top:1px solid #eee !important;">
        {assinatura}
    </div>

</div>
"""
    return html
