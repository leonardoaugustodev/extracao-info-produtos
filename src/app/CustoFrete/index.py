import requests as req

pedidos = ['21357090','21358345','21346456','21360998','21364368','21367158','21367110','21367383','21367298','21368011','21359654','21354998','21340782','21345875','21349373','21377494','21377269','21377557','21371061','21365280','21372527','21364853','21377730','21346907','21365224','21367290','21368377','21376816','21368318','21369431','21369716','21374247','21374727','21377856','21367645','21373840','21336712','21339731','21345442','21341245','21351384','21369232','21369754','21370124','21370160','21370214','21370321','21370322','21370359','21370943','21370533','21371153','21371215','21371277','21371690','21371944','21371971','21372148','21373168','21372205','21373498','21373540','21373484','21373287','21373678','21373842','21373892','21373863','21373169','21374381','21374029','21373841','21374726','21374772','21374888','21375102','21374309','21375156','21375543','21375578','21375403','21375491','21375650','21375624','21375649','21375796','21375953','21375993','21376404','21376405','21376489','21376711','21376950','21338783','21354890','21357302','21365523','21357853','21366324','21344980','21368519','21350696','21360614','21362073','21369546','21370247','21362887','21369972','21370345','21370344','21370904','21371158','21371248','21371249','21371298','21371299','21370422','21369457','21370601','21369739','21369796','21370808','21371943','21372018','21372348','21372655','21372583','21372887','21373035','21373880','21373704','21373947','21373604','21372788','21373483','21373843','21374507','21374432','21374680','21374657','21374724','21374770','21374771','21375021','21374813','21375017','21375490','21375585','21375623','21376050','21376071','21376552','21376643','21376677','21377107','21367593','21372767','21360237','21372763','21370675','21358463','21376676','21366151','21374272','21375097','21365418','21362425','21359069','21372906','21361624','21377865','21371305','21377976','21378058','21378080','21378082']

token = 'Bearer hJ74dY0gxfS8R-bzscqmZAvVjW1FT1HAPWAarjj6QmVRQPZgCDfjwjYPAd01JveNq50JNG8xdIc8pN8D5fD6MqnX2MgqKBylgUJLkbFiIuSr0LMUjvm-P2f9aGT86wjP_7hyQFgtLIMZv4e_NqJHr2-MaI03OxNd5ZjUQqzK9zjNBkrvpGNzbNiOUNIzmhuTOvqhGGFsdq_nkx3lRAQOeZwE3CdJkwprifcQNw44PTNVPaSqmJSrEpGBnAGyNy7aBjL4sl_px0KqDDC3AnB7xKy0yGM'

api_listarTransportadoras = 'http://api.dakotaparts.com.br/Frete/ServicoEntrega/Listar?SomenteAtivos=true'

transportadoras = req.get(api_listarTransportadoras, headers={'Authorization': token}).json()

for pedido in pedidos:

    api_listarPedido = 'http://api.dakotaparts.com.br/Fenix/Frete/Listar?PedidoCodigoExterno={}'.format(pedido)

    api_listarDimensoes = 'http://api.dakotaparts.com.br/Frete/DimensoesPedido/Listar?codigoPedido={}'.format(pedido)
    
    pedidos = req.get(api_listarPedido, headers={'Authorization': token}).json()
    dimensoes = req.get(api_listarDimensoes, headers={'Authorization': token}).json()

    menorValor = 999999

    if len(pedidos) == 0:
        continue

    for transp in transportadoras:

        payload = {
        "Codigo": pedidos[0]['Pedido']['Codigo'],
        "CodigosItensRemovidos": [],
        "ValorItens": pedidos[0]['Pedido']['ValorItens'],
        "PesoCalculado": dimensoes[0]['PesoProdutos'],
        "VolumeCalculado": dimensoes[0]['VolumeProdutos'],
        "Markup": 0,
        "Comprimento": 0,
        "Coleta": 0,
        "Entrega": 0,
        "Cep": pedidos[0]['Pedido']['Endereco']['Cep'],
        "ServicoEntregaCodigo": transp['Codigo'],
        "Conciliacao": False
        }

        api_simulacaoCusto = 'http://api.dakotaparts.com.br/Frete/SimulacaoCusto/SimularPeloPedido'

        resultado = req.post(api_simulacaoCusto, data=payload, headers={'Authorization': token}).json()

        valorSimulado = resultado['ValorSimulado']

        if valorSimulado == None:
            continue
        
        if valorSimulado < menorValor and menorValor > 0:
            menorValor = valorSimulado
            menorTransportadora = transp['Nome']

    print('{0},{1},{2}'.format(pedido, menorTransportadora, menorValor))

        
