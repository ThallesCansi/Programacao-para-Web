async def exemplo_assincrono():
    try:
        await alguma_funcao() # type: ignore
    except Exception as erro:
        raise MinhaExcecao("Erro assíncrono") from erro # type: ignore