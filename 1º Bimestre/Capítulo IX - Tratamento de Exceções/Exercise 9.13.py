# O encadeamento de exceções, também chamado de exception chaining, é uma técnica utilizada para capturar exceção e lançar uma nova exceção com informações adicionais, mantendo o traceback original. Sendo bastante útil quando uma exceção é lançada por uma lib ou módulo que não possui informações suficientes para identificar o erro.