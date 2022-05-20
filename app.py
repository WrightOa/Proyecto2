import streamlit as st
st.title('El Ayudante de  la Pala , ¡Palosa!')
st.header('¡Tan amigable con el ecosistema como contigo!')
option = st.selectbox('¿QUE ESTAS BUSCANDO?',
                     ('Busca aquí :)', 'Insecticidas', 'Fertilizante', 'Desinfectante RBM-Q', 'Abono/Composta/Lumus', 'Sistemas de riego', 'Compuestos químicos', 'Ropa/Vestimenta', 'Herramienta/Maquinaria', 'Semillas', ' '))
st.sidebar.title('¿Quiénes somos?')
st.sidebar.write('Somos una empresa socialmente responsable que busca la eficacia y seguridad de productos químicos en materia de agricultura por medio de nuestra página web, garantizando productos de alta calidad y seguridad en transporte.') 
st.sidebar.balloons()
st.sidebar.image('https://encolombia.com/wp-content/uploads/2021/01/Agricultura-moderna.jpg')
st.sidebar.header('Misión')
st.sidebar.write('Proveer y satisfacer las necesidades de nuestros clientes de una forma mas eficaz, sencilla y segura en materia de agricultura por medio de nuestra página de internet. ')
st.sidebar.header('Visión')
st.sidebar.write('Ser lideres de mercado en materia de agricultura asi como el tener un sector de clientes específicos  asi como clientes fecuentes y confiables.')
st.sidebar.header('Valores')
st.sidebar.markdown("""
* Responsabilidad social
* Calidad
* Honestidad
* Compromiso
* Eficacia  
            """)
st.sidebar.subheader('Autores')
st.sidebar.write('Adrian Wright Olivas')
st.sidebar.write('Gilberto Domínguez Avilés')
st.sidebar.subheader('Dirección')
st.sidebar.write('Facultad de Ciencias Químicas UACH, Universitario, Campus Uach, Chihuahua, Lealtad II, 31125 Chihuahua, Chih., México')
st.image('https://bloglatam.jacto.com/wp-content/uploads/2022/04/agricultura-de-alta-precision-925x308.jpg')
st.header('Algo de reflexionar')
st.subheader('Otras formas de vida, además de la nuestra, merecen nuestra consideración. El hombre debería ser agricultor, no explotador. Este planeta no está destinado exclusivamente a nuestro porvecho. El destruir todas las formas de vida que no tienen para nosotros utilidad ostensible y directa es inmoral y, en definitiva, es muy posible que contribuya a nuestra propia destrucción. "El horticultor autosuficiente" (1978), John Seymour')
st.image('https://i0.wp.com/infoagronomo.net/wp-content/uploads/2017/09/frases-campo.gif?fit=700%2C400&ssl=1')
st.header('-------------------------------------------------------------')
st.sidebar.subheader('¿Cómo utilizar la página?')

if option =='Insecticidas':
  st.subheader('Insecticida Urbano Cipermetrina ')
  st.image('https://www.productoslimpiaya.com/wp-content/uploads/2021/01/cipermetrina.jpg')
  st.write('Es un insecticida con acción de contacto e ingestión, con excelente efecto de derribe y persistencia. Está compuesto por cipermetrina un eficiente insecticida convencional eficiente para cultivos de Algodonero, Maíz, Soya, Frijol y Cebolla')
  st.write('Especificaciones: 80% de concentración en cada 100ml. Contenido neto 2.8lt')
  st.write('Precio:$129.39')
  st.write('Lugar de procedencia: Ojinaga, CHIH.')

  st.subheader('JABÓN POTÁSICO ')
  st.image('https://cdn.shopify.com/s/files/1/0246/3147/6308/products/JabonNuevo2.png?v=1641578067')
  st.write('El jabón potásico (también conocido como potasa) es un potente pesticida naturalque se usa para mantener a raya la proliferación de plagas como pulgones o negrilla.')
  st.write('Especificaciones: 78% de concentración en cada 100 ml. Contenido neto 165 gr.')
  st.write('Precio: $ 179.00 Oferta')
  st.write('Lugar de procedencia: Delicias, CHIH.')


  
if option =='Fertilizante':
  st.subheader('Abono Organico Humato Potasico ')
  st.image('https://http2.mlstatic.com/D_NQ_NP_876248-MLM31369916766_072019-W.jpg')
  st.write('El humato potásico es un producto que se presenta en forma de polvo 100% soluble en agua, muy concentrado y que aporta materia orgánica y potasio, por lo que no solo mejora los suelos a nivel físico, químico y biológico, sino que también proporciona uno de los tres elementos primarios que toda planta necesita.')
  st.write('Especificaciones: 5Kg Fertilizante natural:aplicado al suelo solo sepultado para mayor eficiencia')
  st.write('Precio: 568$')
  st.write('Lugar de procedencia: Culiacan sinaloa')

  st.subheader('HARINA DE ROCAS ')
  st.image('https://http2.mlstatic.com/D_NQ_NP_963227-MLM43943671539_102020-O.jpg')
  st.write('Harina de Roca es un producto creado y utilizado como fertilizante para suelos, gracias a su mezcla de minerales como Sílice, Hierro, Calcio, Magnesio, Fósforo, Manganesio, Cobre y Zinc, tiene la capacidad de revitalizar el suelo nutriéndolo de minerales que permiten un mejor suelo para tener buen desarrollo en los cultivos')
  st.write('Especificaciones:2Kg Minerales Abono Fertilizante Natural')
  st.write('Precio:299$')
  st.write('Lugar de procedencia: Chihuahua, chihuahua')


if option =='Desinfectante RBM-Q':
  st.subheader('Desinfectante Rbm-tc Organico ')
  st.image('https://cdn.shopify.com/s/files/1/0101/5775/2383/products/19.RBM_TC_1L_3543x.jpg?v=1612798092.jpg')
  st.write('Es un desinfectante organico formulado a base de semillas de mandarina de amplio espectro contra bacterias,virus,hongis y esporas')
  st.write('Especificaciones:1Lt, Desinfectante natural a base de extracto de semillas de citricos')
  st.write('Precio:1,058$')
  st.write('Lugar de procedencia:San Miguel De Allende Guanajuato')
  st.subheader('Sanitizante concentrado para termonebulizador ')
  st.image('https://http2.mlstatic.com/D_NQ_NP_922961-MLM43510359356_092020-O.jpg')
  st.write('Desinfecta y sanitiza todas las superficies al igual que diferentes tipos de hortalizas sin ser invasibos con la planta o con el fruto ')
  st.write('120mL,Especificaciones:Ecologico,No corrosivo,Biodegradable libre de fosfatos')
  st.write('Precio:179$')
  st.write('Lugar de procedencia:Atizapan De Zaragoza Edo de Mexico')

if option =='Abono/Composta/Lumus':
  st.subheader('Humus de lombriz ')
  st.image('https://th.bing.com/th/id/R.ea5345e69eef3ec6dd2c7bf6f2951db5?rik=LFV1mIjpyTWL9w&pid=ImgRaw&r=0')
  st.write('En Plásticos y Papeles Viedma disponemos de bolsas para humus, abonos y forraje. Este tipo de embalaje permite transportar grandes cargas pesadas sin riesgo a rotura. El humus de lombriz es uno de los abonos orgánicos más populares del mercado.')
  st.write('Especificaciones: 5 kg por costal')
  st.write('Precio: $359')
  st.write('Lugar de procedencia: Ojinaga, CHIH.')

  st.subheader('ABONO VERMILITA')
  st.image('https://th.bing.com/th/id/R.3d0dfc258a737512bc9395233e902490?rik=2HenEF5d0i8RdA&riu=http%3a%2f%2fcdn.shopify.com%2fs%2ffiles%2f1%2f1457%2f1446%2fproducts%2fVermiculita_Sustrato_grande.jpg%3fv%3d1484349473&ehk=dxwCDNldE92ff6%2bVGQ%2fFRjfVt66XifzpBylKsnyJuh4%3d&risl=&pid=ImgRaw&r=0')
  st.write('Abono Orgánico Fermentado tipo Bocashi Costal con 19 litros.')
  st.write('Modo de Empleo: mezclar con la tierra ó sustrato evitando aplicar directamente en la zona de raíces, regar abundantemente después de la aplicación.')
  st.write('Especificaciones:Aplicar cada 15 días en hortalizas, hierbas, plantas ornamentales y cada 4 meses en árboles. ')
  st.write('Precio: $149.99')
  st.write('Lugar de procedencia: Fabrica las huertas Michoacan, Méxcio.')

if option =='Sistemas de riego':
  st.subheader('Lieneas de goteo ')
  st.image('https://es.chinadrip.com/uploadfile/202001/10/c2224e123ba72f8acebc788b4c618cc6_medium.jpg')
  st.write('La linea de goteo economica desarrollada para el riego por goteo subterraneo con proteccion contra taponamiento y mecanismo anti raices.')
  st.write('Especificaciones:20 m')
  st.write('Precio: 600$')
  st.write('Lugar de procedencia: Torreon, coahuila')

  st.subheader('Aspersor ')
  st.image('https://www.traxco.es/blog/wp-content/uploads/2020/07/aspersores-de-riego.jpg')
  st.write('Para los productores de hortalizas de campo abierto que buscan lograr una excelente uniformidad de cultivos con un espaciamiento amplio y variado por encima de los 10m, los aspersores de impacto 3D D-Net ofrecen la maxima eficiencia en el uso del agua')
  st.write('Especificaciones: Distribución del agua magníficamente uniforme con la máxima eficiencia de uso del agua. Rendimiento duradero y mantenimiento que ahorra mano de obra. ')
  st.write('Precio: 3690$')
  st.write('Lugar de procedencia: Los mochis, Sinaloa')

if option =='Compuestos químicos':
  st.subheader('RODENTICIDA/CEBO ENVENENADO DE 250 GRAMOS ROJO RATIDEL-B ')
  st.image('https://http2.mlstatic.com/D_NQ_NP_728088-MLM47065517143_082021-W.jpg')
  st.write('Rodenticida/ Cebo Envenenado Ratidel-B en presentación de 250 gramos, combate eficazmente la aparición de roedores gracias a sus ingredientes de primera calidad. Compuesto de bromadilona al .005% con saborizante y semillas, es de fácil aceptación y atrae fácilmente a los animales para su eliminación. Es un producto anticoagulante que permite ser empleado en interiores y exteriores, sin dejar olores o desechos desagradables debido a que cuenta con una fórmula que se encarga de secar los órganos del roedor sin que sus restos huelan mal.')
  st.write('Especificaciones:Largo	13.9 cm	Ancho	7.7 cm')
  st.write('Precio: 98$')
  st.write('Lugar de procedencia: Del.Coyoacan')

  st.subheader('Saf-t-side 0.946 Imex Insecticida Y Acaricida ')
  st.image('https://http2.mlstatic.com/D_NQ_NP_711307-MLM48348687974_112021-W.jpg')
  st.write('Un acaricida es un plaguicida que se utiliza para eliminar, controlar o prevenir la presencia o acción de los ácaros mediante una acción química. Los ácaros son arácnidos diminutos de cuerpo ovalado en los que la cabeza, tórax y abdomen se encuentran fusionados en un cuerpo no segmentado.')
  st.write('Especificaciones: Aceite parafinico de petroleo al 80 %')
  st.write('Precio: 369$')
  st.write('Lugar de procedencia: Tecoman, Colima')

if option =='Ropa/Vestimenta':
  st.subheader(' Oberol de carga ')
  st.image('https://th.bing.com/th/id/R.d068d3b4ea081c5631edd13ee02db6fd?rik=CdVPXQlgWe%2fyOQ&pid=ImgRaw&r=0')
  st.write(' Oberol de color rojo para trabajos pesados, riesgosamente quimicos, biológicos y químico-biológicos.')
  st.write('Especificaciones: todas las tallas disponibles')
  st.write('Precio: mayoreo: $299    menudeo: $199')
  st.write('Lugar de procedencia: Leon, Guanajuato.')

  st.subheader('Masacaras KN95 ')
  st.image('https://th.bing.com/th/id/OIP.aBmOE_-xmwm5wl6ACDfdngHaHa?pid=ImgDet&rs=1')
  st.write('Mascarilla KN95 tipo quirurgica de color blanco, todos modelos disponibles.')
  st.write('Especificaciones: color blanco')
  st.write('Precio: precio por unidad $300')
  st.write('Lugar de procedencia: Guadalajara, México.')

if option =='Herramienta/Maquinaria':
  st.subheader('Tractor agrícola 4850 John Deer ')
  st.image('https://th.bing.com/th/id/R.3f3bac58ac083b717fdcc2fd1f428177?rik=nbYvRJWYvwKJWA&pid=ImgRaw&r=0')
  st.write(' Tractor agrícola John Deer 4850, año 1998, procedencia Dallas, Tx.')
  st.write('Especificaciones: Fallas de bateria')
  st.write('Precio: negociable +$600,000.00')
  st.write('Lugar de procedencia: Cd. Juarez, Chihuahua.')

  st.subheader('Pala Frontal Para Tractores Agricolas Massey Ferguson ')
  st.image('https://th.bing.com/th/id/R.9e52705b7aa59a0d9e7bb561288a0bee?rik=%2fpuvzLQs%2bHsF%2fA&pid=ImgRaw&r=0')
  st.write('PALA FRONTAL PARA TRACTORES MASSEY FERGUSON ( 255, 265, 275, 285, 355, 365, 375, 385 ) o QUE TENGA BASE PARA ATORNILLAR EN LA PARTE DE ENFRENTE ARRIBA DEL EJE EN CUADRO CON 4 PERFORACIONES, PARA TRACTORES DE 60 A 100 HP.ver las ultimas fotos se muestra como son las bases y las perforaciones necesarias en el tractor para atornillas.')
  st.write('Especificaciones: Color rojo')
  st.write('Precio: $180,000')
  st.write('Lugar de procedencia: Hermosillo, Sonora.')

if option =='Semillas':
  st.subheader('Paquete de semilla de Sandia Roja Sunsugar Syngenta. ')
  st.image('https://http2.mlstatic.com/D_NQ_NP_940076-MLM44128107600_112020-O.webp')
  st.write('El tamaño y forma de la fruta es larga, cuyo peso oscila entre los 12 20 kg., de color verde claro, con estrias verde obscuro; tiene una larga vida de anaquel y soporta muy bien la transportacion. Las semillas son pequeñas de color face obscuro. El color de la carne es rojo brillante. Los dias de la maduracion oscilan alrededor de los 90 dias. Resistencia a enfermedades mas comunes')
  st.write('Especificaciones:Paquete de Libra de alrededor 8000 semillas por libra.')
  st.write('Precio:Precio de mostrados en para compra en directo con nosotros en 117 USD aprox 2500 + envio de 200 pesos a todo Mexico. Se cotiza al tipo de cambio')
  st.write('Lugar de procedencia: San Antonio, Tx.')

  st.subheader('Semilla orgánica de trigo')
  st.image('https://http2.mlstatic.com/D_NQ_NP_870872-MLM49669138771_042022-O.webp')
  st.write('Los germinados son alimentos vivos y esto aumenta su valor nutricional que se mantiene intacto hasta el momento en que se come.')
  st.write('Especificaciones: Trigo, semilla orgánica, ideal para germinados y preparaciones culinarias 2 Kg')
  st.write('Precio: $298')
  st.write('Lugar de procedencia: Oaxaca, México.')
video_file = open('Adrian1.mp4', 'rb')
video_bytes = video_file.read()

st.sidebar.video(video_bytes)
