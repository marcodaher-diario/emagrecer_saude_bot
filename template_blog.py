# -*- coding: utf-8 -*-

def formatar_texto(texto):
    """
    Processa o corpo do texto: H2 para títulos curtos e P para o restante.
    """
    if not texto:
        return ""
        
    linhas = [l.strip() for l in texto.split("\n") if l.strip()]
    html_final = ""
    COR_MD = "rgb(7, 55, 99)"
    
    for linha in linhas:
        e_titulo = linha.startswith("#")
        linha_limpa = linha.strip("#* ").strip()

        # Ordem 5: H2 Arial 20 Bold, Esquerda, Azul Marinho, Maiúsculas
        if e_titulo or (len(linha_limpa.split()) <= 18 and not linha_limpa.endswith(".")):
            html_final += f"""
            <h2 style="text-align:left !important; font-family:Arial !important; color:{COR_MD} !important; 
                       font-size:20px !important; font-weight:bold !important; text-transform:uppercase !important; 
                       margin-top:25px !important; margin-bottom:10px !important;">
                {linha_limpa}
            </h2>
            """
        else:
            # Ordem 6: Texto 18 Justificado, Azul Marinho
            html_final += f"""
            <p style="text-align:justify !important; font-family:Arial !important; color:{COR_MD} !important; 
                      font-size:18px !important; line-height:1.6 !important; margin-bottom:15px !important;">
                {linha_limpa}
            </p>
            """
    return html_final

def obter_esqueleto_html(dados):
    """
    Monta o HTML completo garantindo a exibição do Título H3 acima da imagem.
    """
    # Verificação de segurança para as chaves do dicionário
    titulo = dados.get("titulo", "TÍTULO NÃO ENCONTRADO")
    imagem = dados.get("imagem", "")
    texto_completo = dados.get("texto_completo", "")
    assinatura = dados.get("assinatura", "")

    conteudo_formatado = formatar_texto(texto_completo)
    COR_MD = "rgb(7, 55, 99)"

    return f"""
<div style="max-width:900px !important; margin:auto !important; font-family:Arial, sans-serif !important;">

    <div style="text-align:center !important; font-family:Arial !important; font-size:28px !important; 
                font-weight:bold !important; color:{COR_MD} !important; text-transform:uppercase !important; 
                margin-bottom:25px !important; line-height: 1.2 !important;">
        {titulo}
    </div>

    <div style="text-align:center !important; margin-bottom:25px !important;">
        <img src="{imagem}" style="width:100% !important; height:auto !important; border-radius:8px !important; display:block !important; margin:auto !important;">
    </div>

    <div>
        {conteudo_formatado}
    </div>

    <div style="margin-top:40px !important; padding-top:20px !important; border-top:1px solid #eee !important; color:{COR_MD} !important;">
        {assinatura}
    </div>

</div>
"""
