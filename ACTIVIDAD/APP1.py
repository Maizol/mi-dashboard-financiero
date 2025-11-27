from flask import Flask, render_template_string

app = Flask(__name__)

# --- DATOS DE LA CAMPAÑA (MEJORADO CON IMÁGENES LOCALES Y MÁS CONTENIDO) ---
campaign = {
    "hero": {
        "title_left": "MAESTRÍA\nARTESANAL",
        "title_right": "INGENIERÍA\nDE CONFORT",
        "subtitle": "Envíos gratis a todo el Perú desde S/149. Cambios fáciles en tienda.",
        "cta": "VER NOVEDADES 2025",
        "discount": "25% OFF",
        "discount_text": "Primera compra"
    },
    "stats": [
        {"number": "60+", "label": "Años de tradición"},
        {"number": "40%", "label": "Más ligero"},
        {"number": "12h", "label": "Comodidad garantizada"}
    ],
    "carousel": [
        {
            "type": "img", 
            "src": "https://images.pexels.com/photos/1032110/pexels-photo-1032110.jpeg?auto=compress&cs=tinysrgb&w=800", 
            "year": "1980", 
            "title": "Innovando desde el inicio",
            "desc": "Nuestra planta en Ate: donde la tradición del cuero comenzó hace más de 60 años.",
            "cta": "Conoce nuestra historia",
            "badge": "Herencia Peruana"
        },
        {
            "type": "vid", 
            "src": "https://cdn.pixabay.com/video/2022/05/30/119035-716946024_tiny.mp4",
            "poster": "https://images.pexels.com/photos/1598505/pexels-photo-1598505.jpeg?auto=compress&cs=tinysrgb&w=800",
            "year": "2025", 
            "title": "Tecnología Flexible", 
            "desc": "Suelas con memoria que se adaptan a tu pisada sin perder su forma original.",
            "cta": "Ver tecnología",
            "badge": "Innovation Lab"
        },
        {
            "type": "icon", 
            "year": "TECH", 
            "title": "Ultralight + Memory Foam", 
            "desc": "Sistema de doble densidad: 40% más ligero que el cuero tradicional.",
            "cta": "Especificaciones técnicas",
            "features": ["Suela EVA", "Plantilla Memory", "Cuero Premium"]
        },
        {
            "type": "life", 
            "src": "https://images.pexels.com/photos/7679454/pexels-photo-7679454.jpeg?auto=compress&cs=tinysrgb&w=800", 
            "year": "HOY", 
            "title": "Camina la historia", 
            "desc": "Para el arquitecto moderno: estilo Smart Casual que resiste jornadas de 12 horas.",
            "cta": "Ver colección",
            "badge": "Smart Casual"
        }
    ],
    "influencers": [
        {
            "name": "Shirley Palomino", 
            "role": "Diseño & Estilo", 
            "review": "Después de 12 horas de shooting, mis pies siguen intactos. La mezcla de cuero real con esta suela es irreal.", 
            "img": "https://randomuser.me/api/portraits/women/44.jpg",
            "social": "@shirleypalomino",
            "rating": 5
        },
        {
            "name": "Alfredo Bonifaz", 
            "role": "Traveler / Blog", 
            "review": "Caminé todo el centro histórico. Aguantan el ritmo urbano sin perder la elegancia del Smart Casual.", 
            "img": "https://randomuser.me/api/portraits/men/32.jpg",
            "social": "@worldtravelerab",
            "rating": 5
        }
    ],
    "products": [
        {"name": "Oxford Classic", "price": "S/ 299", "img": "https://images.pexels.com/photos/1598508/pexels-photo-1598508.jpeg?auto=compress&cs=tinysrgb&w=400", "discount": "S/ 239"},
        {"name": "Loafer Ultralight", "price": "S/ 349", "img": "https://images.pexels.com/photos/19090/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=400", "discount": "S/ 279"},
        {"name": "Derby Memory", "price": "S/ 379", "img": "https://images.pexels.com/photos/292999/pexels-photo-292999.jpeg?auto=compress&cs=tinysrgb&w=400", "discount": "S/ 299"}
    ],
    "faqs": [
        {"q": "¿Cómo cuidar el cuero?", "a": "Usa crema nutritiva cada 15 días y cepillo suave."},
        {"q": "¿Tienen garantía?", "a": "Sí, 6 meses contra defectos de fabricación."},
        {"q": "¿Envíos a provincias?", "a": "Envíos gratis desde S/149 a todo Perú."}
    ],
    "social_feed": [
        {"platform": "instagram", "handle": "@calimod_oficial", "followers": "125K"},
        {"platform": "facebook", "handle": "/CalimodPeru", "followers": "200K"},
        {"platform": "tiktok", "handle": "@calimod", "followers": "45K"}
    ]
}

html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calimod: Legado en Movimiento</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Montserrat:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        /* --- ESTILOS MAESTROS --- */
        body { font-family: 'Montserrat', sans-serif; overflow-x: hidden; cursor: none; /* Ocultamos cursor default */ }
        .font-serif { font-family: 'Playfair Display', serif; }
        
        /* Cursor Personalizado */
        #cursor { width: 20px; height: 20px; border: 2px solid #e5b985; border-radius: 50%; position: fixed; pointer-events: none; z-index: 9999; transition: transform 0.1s ease; transform: translate(-50%, -50%); mix-blend-mode: difference; }
        
        /* Splash Screen (Carga) */
        #loader { position: fixed; inset: 0; bg-black; z-index: 10000; background: #111; display: flex; justify-content: center; align-items: center; transition: opacity 0.8s ease; }
        
        /* Scroll Reveal (Aparecer al bajar) */
        .reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s ease-out; }
        .reveal.active { opacity: 1; transform: translateY(0); }

        /* Split Screen Refinado */
        .split-container { display: flex; height: 95vh; overflow: hidden; position: relative; }
        .split { flex: 1; transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1); position: relative; display: flex; align-items: center; justify-content: center; flex-direction: column; }
        .split:hover { flex: 1.6; }
        
        .split-left { background: linear-gradient(to bottom, rgba(30, 20, 10, 0.9), rgba(42, 27, 18, 0.8)), url('https://www.transparenttextures.com/patterns/dark-leather.png'); color: #e5b985; }
        .split-right { background: #fff; color: #1e3a8a; }

        /* Carrusel MEJORADO con navegación */
        .carousel-card { transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); height: 100%; display: flex; flex-direction: column; }
        .carousel-card:hover { transform: translateY(-10px); }
        .carousel-img-container { height: 280px; position: relative; overflow: hidden; }
        .text-clamp { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        
        /* Botones de navegación carrusel */
        .carousel-nav { position: absolute; top: 50%; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; backdrop-filter: blur(10px); transition: all 0.3s; }
        .carousel-nav:hover { background: rgba(0,0,0,0.8); transform: translateY(-50%) scale(1.1); }
        .carousel-nav.left { left: -20px; }
        .carousel-nav.right { right: -20px; }
        
        /* Modal mejorado */
        .modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.95); z-index: 9999; align-items: center; justify-content: center; backdrop-filter: blur(20px); }
        .modal.active { display: flex; animation: fadeIn 0.3s ease; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        
        /* Video player mejorado */
        video { border-radius: 10px; box-shadow: 0 20px 60px rgba(0,0,0,0.5); max-width: 90%; max-height: 80vh; }

        /* Zapato Interactivo */
        .shoe-elastic { transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275); cursor: pointer; }
        .bend-active { transform: rotate(-35deg) scale(0.9) skewX(-10deg) !important; filter: drop-shadow(0 0 15px rgba(255, 255, 255, 0.5)); }

        /* Animaciones SVG */
        .svg-icon { animation: float 4s ease-in-out infinite; }
        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
        
        /* MEJORA 28: Smooth scroll para toda la página */
        html { scroll-behavior: smooth; }
        
        /* MEJORA 29: Scrollbar personalizado */
        ::-webkit-scrollbar { width: 10px; height: 10px; }
        ::-webkit-scrollbar-track { background: #f1f1f1; }
        ::-webkit-scrollbar-thumb { background: #888; border-radius: 5px; }
        ::-webkit-scrollbar-thumb:hover { background: #555; }
        
        /* MEJORA 30: Animaciones de entrada */
        @keyframes slideUp { from { opacity: 0; transform: translateY(50px); } to { opacity: 1; transform: translateY(0); } }
        .reveal { animation: slideUp 0.8s ease-out forwards; }
        
        /* MEJORA 31: Efecto parallax en hero */
        @media (min-width: 768px) {
            .split:hover .text-center { transform: scale(1.05) translateZ(0); }
        }
        
        /* MEJORA 32: Ripple effect en botones */
        button { position: relative; overflow: hidden; }
        button::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }
        button:active::after {
            width: 300px;
            height: 300px;
        }
        
        /* MEJORA 33: Skeleton loading */
        .skeleton {
            background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
            background-size: 200% 100%;
            animation: loading 1.5s infinite;
        }
        @keyframes loading {
            0% { background-position: 200% 0; }
            100% { background-position: -200% 0; }
        }
        
        /* MEJORA 34: Glass morphism */
        .glass {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        /* MEJORA 35: Navbar sticky mejorado */
        #navbar.scrolled {
            padding: 12px 32px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body class="bg-gray-50 selection:bg-yellow-500 selection:text-white">

    <div id="cursor"></div>

    <div id="loader">
        <div class="text-center">
            <h1 class="text-4xl text-[#e5b985] font-serif tracking-widest animate-pulse">CALIMOD</h1>
            <p class="text-gray-500 text-xs mt-2 uppercase tracking-[0.5em]">Cargando Experiencia</p>
        </div>
    </div>

    <nav class="fixed top-0 w-full z-50 bg-black/90 backdrop-blur-sm text-white py-4 px-8 flex justify-between items-center border-b border-gray-800 transition-all duration-300" id="navbar">
        <div class="text-xl font-serif tracking-widest text-[#e5b985]">CALIMOD</div>
        <div class="hidden md:flex gap-6 text-xs font-bold tracking-widest text-gray-400">
            <span class="hover:text-white cursor-pointer transition">COLECCIÓN</span>
            <span class="hover:text-white cursor-pointer transition">HISTORIA</span>
            <span class="hover:text-white cursor-pointer transition">TECNOLOGÍA</span>
        </div>
        <button class="bg-[#e5b985] text-black px-4 py-2 text-xs font-bold uppercase rounded hover:bg-white transition">Comprar</button>
    </nav>

    <header class="split-container pt-16">
        <div class="split split-left px-4 group">
            <div class="text-center transform transition duration-700 group-hover:scale-105">
                 <p class="uppercase tracking-[0.4em] text-[10px] mb-4 text-yellow-600 font-bold border-b border-yellow-600 inline-block pb-1">Since 1964</p>
                <h1 class="font-serif text-5xl md:text-7xl mb-4 leading-tight font-bold">{{ data.hero.title_left.replace('\n', '<br>')|safe }}</h1>
                <p class="opacity-60 text-sm max-w-xs mx-auto">La tradición no se fabrica, se hereda.</p>
                
                <!-- MEJORA 1: Estadísticas dinámicas -->
                <div class="flex justify-center gap-8 mt-8">
                    {% for stat in data.stats %}
                    <div class="text-center">
                        <div class="text-3xl font-bold text-yellow-400">{{ stat.number }}</div>
                        <div class="text-[10px] text-gray-400 uppercase tracking-wide">{{ stat.label }}</div>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
        
        <div class="split split-right px-4 group relative">
            <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/graphy.png')] opacity-10"></div>
            <div class="text-center transform transition duration-700 group-hover:scale-105 z-10">
                <p class="uppercase tracking-[0.4em] text-[10px] mb-4 text-blue-600 font-bold border-b border-blue-600 inline-block pb-1">Future Ready</p>
                <h1 class="font-bold text-5xl md:text-7xl mb-4 leading-tight text-slate-900">{{ data.hero.title_right.replace('\n', '<br>')|safe }}</h1>
                
                <!-- MEJORA 2: Badge de descuento -->
                <div class="inline-block bg-red-500 text-white px-4 py-2 rounded-full font-bold text-sm mb-4 animate-pulse">
                    {{ data.hero.discount }} - {{ data.hero.discount_text }}
                </div>
                
                <div class="bg-white/80 backdrop-blur shadow-2xl p-6 rounded-xl mt-4 border-l-4 border-blue-600 max-w-sm mx-auto">
                    <p class="text-xs font-bold text-gray-500 mb-2 uppercase tracking-wide">Oferta de Lanzamiento</p>
                    <p class="text-sm font-medium text-gray-800 mb-4">{{ data.hero.subtitle }}</p>
                    <button onclick="scrollToProducts()" class="w-full bg-black text-white py-3 text-xs font-bold tracking-[0.2em] hover:bg-gray-800 transition transform hover:-translate-y-1 shadow-lg">
                        {{ data.hero.cta }}
                    </button>
                    
                    <!-- MEJORA 3: Trust badges -->
                    <div class="flex justify-around mt-4 pt-4 border-t border-gray-200">
                        <div class="text-center">
                            <div class="text-lg">🚚</div>
                            <div class="text-[9px] text-gray-500">Envío gratis</div>
                        </div>
                        <div class="text-center">
                            <div class="text-lg">🔄</div>
                            <div class="text-[9px] text-gray-500">Cambio fácil</div>
                        </div>
                        <div class="text-center">
                            <div class="text-lg">✅</div>
                            <div class="text-[9px] text-gray-500">Garantía 6m</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <section class="py-24 bg-white relative">
        <div class="container mx-auto px-4 reveal">
            <div class="flex justify-between items-end mb-12 px-4">
                <div>
                    <span class="text-blue-600 font-bold tracking-widest uppercase text-xs">Social Media</span>
                    <h2 class="text-3xl md:text-4xl font-bold mt-2 text-gray-900">De la Fábrica a tu Futuro</h2>
                </div>
                <div class="hidden md:flex gap-4 items-center">
                    <!-- MEJORA 4: Botones de navegación visibles -->
                    <button onclick="scrollCarousel('left')" class="bg-black text-white px-4 py-2 rounded-full hover:bg-gray-800 transition">←</button>
                    <button onclick="scrollCarousel('right')" class="bg-black text-white px-4 py-2 rounded-full hover:bg-gray-800 transition">→</button>
                </div>
            </div>
            
            <div id="carousel-container" class="flex overflow-x-auto gap-6 pb-12 snap-x snap-mandatory px-4 scroll-smooth" style="scrollbar-width: none;">
                {% for slide in data.carousel %}
                <div class="flex-none w-80 snap-center">
                    <div class="carousel-card bg-white rounded-xl shadow-xl overflow-hidden border border-gray-100 hover:shadow-2xl">
                        <div class="carousel-img-container bg-gray-100 relative group">
                            {% if slide.type == 'img' %}
                                <img src="{{ slide.src }}" alt="{{ slide.title }}" class="w-full h-full object-cover transition duration-700 group-hover:scale-110" loading="lazy">
                                <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
                                <div class="absolute bottom-4 left-4 text-white">
                                    <span class="bg-[#e5b985] text-black text-[10px] px-2 py-1 font-bold rounded mb-2 inline-block">{{ slide.year }}</span>
                                </div>
                                <!-- MEJORA 5: Badge de categoría -->
                                {% if slide.badge %}
                                <div class="absolute top-4 right-4 bg-white/90 backdrop-blur text-black text-[9px] px-2 py-1 font-bold rounded shadow-sm">{{ slide.badge }}</div>
                                {% endif %}
                            {% elif slide.type == 'vid' %}
                                <img src="{{ slide.poster }}" alt="{{ slide.title }}" class="w-full h-full object-cover" loading="lazy">
                                <!-- MEJORA 6: Video funcional al hacer clic -->
                                <div class="absolute inset-0 flex items-center justify-center bg-black/20 group-hover:bg-transparent transition cursor-pointer" onclick="openVideoModal('{{ slide.src }}')">
                                    <div class="w-12 h-12 bg-white/90 rounded-full flex items-center justify-center pl-1 shadow-lg backdrop-blur">▶</div>
                                </div>
                                <div class="absolute top-4 left-4 bg-blue-600 text-white text-[10px] px-2 py-1 font-bold rounded shadow-sm">{{ slide.year }}</div>
                                {% if slide.badge %}
                                <div class="absolute top-4 right-4 bg-white/90 backdrop-blur text-black text-[9px] px-2 py-1 font-bold rounded shadow-sm">{{ slide.badge }}</div>
                                {% endif %}
                            {% elif slide.type == 'icon' %}
                                <div class="w-full h-full flex flex-col items-center justify-center bg-gradient-to-br from-blue-50 to-blue-100 text-blue-600 gap-4 p-8 text-center">
                                    <svg class="svg-icon w-16 h-16 fill-current" viewBox="0 0 24 24"><path d="M20.57 3.43a1.1 1.1 0 0 0-1.56 0l-8.45 8.45c-.2.2-.36.44-.45.7L8.24 17c-.1.28-.03.6.16.8.2.2.5.25.78.16l4.42-1.86c.25-.1.5-.26.7-.45l8.45-8.45c.44-.43.44-1.13 0-1.56l-2.18-2.21z"/></svg>
                                    <span class="font-bold text-sm tracking-wider">ULTRALIGHT</span>
                                    <!-- MEJORA 7: Lista de features -->
                                    {% if slide.features %}
                                    <div class="flex gap-2 flex-wrap justify-center mt-2">
                                        {% for feature in slide.features %}
                                        <span class="bg-blue-600 text-white text-[8px] px-2 py-1 rounded-full">{{ feature }}</span>
                                        {% endfor %}
                                    </div>
                                    {% endif %}
                                </div>
                            {% else %}
                                <img src="{{ slide.src }}" alt="{{ slide.title }}" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition duration-500" loading="lazy">
                                <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
                                <div class="absolute bottom-4 left-4 text-white font-bold">{{ slide.year }}</div>
                                {% if slide.badge %}
                                <div class="absolute top-4 right-4 bg-white/90 backdrop-blur text-black text-[9px] px-2 py-1 font-bold rounded shadow-sm">{{ slide.badge }}</div>
                                {% endif %}
                            {% endif %}
                        </div>
                        
                        <div class="p-6 flex-1 flex flex-col justify-between h-40">
                            <div>
                                <h4 class="font-bold text-lg mb-2 text-gray-900 leading-tight">{{ slide.title }}</h4>
                                <p class="text-sm text-gray-500 leading-relaxed text-clamp">{{ slide.desc }}</p>
                            </div>
                            <!-- MEJORA 8: Botón "Ver más" funcional -->
                            <div class="mt-4 flex justify-between items-center border-t pt-3 border-gray-100">
                                {% if slide.cta %}
                                <button onclick="showSlideDetail({{ loop.index0 }})" class="text-[10px] font-bold text-blue-600 uppercase tracking-wider hover:text-blue-800 transition">{{ slide.cta }} →</button>
                                {% else %}
                                <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider">Ver más</span>
                                {% endif %}
                                <span class="text-gray-300 text-xs">{{ loop.index }}/4</span>
                            </div>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- MEJORA 9: Modal para videos -->
    <div id="video-modal" class="modal">
        <button onclick="closeVideoModal()" class="absolute top-8 right-8 text-white text-4xl hover:scale-110 transition">×</button>
        <video id="modal-video" controls autoplay class="max-w-4xl">
            <source src="" type="video/mp4">
        </video>
    </div>

    <section class="py-24 bg-[#0a0a0a] text-white overflow-hidden relative border-t border-gray-800">
        <div class="container mx-auto px-4 flex flex-col lg:flex-row items-center justify-center gap-16 reveal">
            <div class="lg:w-1/3 text-center lg:text-left z-10">
                <span class="text-green-400 font-bold tracking-widest uppercase text-xs mb-4 block animate-pulse">● Live Demo</span>
                <h2 class="text-4xl md:text-5xl font-serif mb-6">Prueba de <br><span class="text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-[#e5b985]">Flexibilidad</span></h2>
                <p class="text-gray-400 mb-8 font-light">Interactúa con el simulador móvil para desbloquear tu descuento estudiantil.</p>
                
                <div id="success-box" class="hidden transform transition-all duration-500 translate-y-4 opacity-0">
                    <div class="bg-green-900/30 border border-green-500/50 p-4 rounded-lg flex items-center gap-4">
                        <div class="bg-green-500 text-black w-8 h-8 rounded-full flex items-center justify-center font-bold">✓</div>
                        <div>
                            <p class="text-green-400 font-bold text-sm">CÓDIGO ACTIVO</p>
                            <p class="text-white font-mono text-xl tracking-widest">STORIES10</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="phone-mockup relative bg-black rounded-[3rem] border-8 border-[#222] shadow-2xl h-[600px] w-[320px] overflow-hidden select-none">
                <div class="w-full h-full bg-gradient-to-b from-gray-800 to-black relative flex flex-col items-center pt-12">
                    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-32 h-6 bg-[#222] rounded-b-xl z-20"></div>
                    
                    <div class="w-full px-4 mb-8 flex gap-1">
                        <div class="h-1 flex-1 bg-white rounded-full"></div>
                        <div class="h-1 flex-1 bg-white/30 rounded-full"></div>
                    </div>
                    
                    <h3 class="text-2xl font-bold mb-2">¿AGUANTA? 🤔</h3>
                    <p class="text-xs text-gray-400 mb-10">Presiona el zapato para doblarlo</p>
                    
                    <div class="text-[8rem] shoe-elastic filter grayscale brightness-75 transition-all duration-100 z-10"
                         id="shoe-btn"
                         onmousedown="bendShoe()"
                         onmouseup="releaseShoe()"
                         ontouchstart="bendShoe()"
                         ontouchend="releaseShoe()">
                        👞
                    </div>

                    <div id="finger-hint" class="absolute top-1/2 left-1/2 -translate-x-1/2 translate-y-10 text-4xl animate-bounce pointer-events-none opacity-80">👆</div>

                    <div class="absolute bottom-10 w-3/4 bg-white text-black rounded-lg flex text-xs font-bold py-3 shadow-lg transform -rotate-2">
                        <div class="w-1/2 text-center border-r border-gray-200">SE ROMPE</div>
                        <div class="w-1/2 text-center text-green-600">FLEXIBLE</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- MEJORA 10: Sección de productos -->
    <section id="productos" class="py-24 bg-gray-50">
        <div class="container mx-auto px-4 reveal">
            <h2 class="text-4xl font-bold text-center mb-12">Colección Destacada</h2>
            <div class="grid md:grid-cols-3 gap-8">
                {% for product in data.products %}
                <div class="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-2xl transition group">
                    <div class="h-64 overflow-hidden bg-gray-100">
                        <img src="{{ product.img }}" alt="{{ product.name }}" class="w-full h-full object-cover group-hover:scale-110 transition duration-700">
                    </div>
                    <div class="p-6">
                        <h3 class="font-bold text-xl mb-2">{{ product.name }}</h3>
                        <div class="flex items-center gap-3 mb-4">
                            <span class="text-2xl font-bold text-blue-600">{{ product.discount }}</span>
                            <span class="text-gray-400 line-through">{{ product.price }}</span>
                            <span class="bg-red-500 text-white text-xs px-2 py-1 rounded-full font-bold">-20%</span>
                        </div>
                        <button class="w-full bg-black text-white py-3 rounded-lg font-bold hover:bg-gray-800 transition">
                            Agregar al Carrito
                        </button>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- MEJORA 11: Testimonios de influencers mejorados -->
    <section class="py-24 bg-white">
        <div class="container mx-auto px-4 reveal">
            <div class="text-center mb-12">
                <span class="text-blue-600 font-bold tracking-widest uppercase text-xs">Testimonios Reales</span>
                <h2 class="text-4xl font-bold mt-2">Lo que dicen los expertos</h2>
            </div>
            <div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                {% for inf in data.influencers %}
                <div class="bg-gray-50 rounded-xl p-8 shadow-lg hover:shadow-xl transition">
                    <div class="flex items-center gap-4 mb-4">
                        <img src="{{ inf.img }}" alt="{{ inf.name }}" class="w-16 h-16 rounded-full object-cover border-4 border-white shadow-lg">
                        <div>
                            <h4 class="font-bold text-lg">{{ inf.name }}</h4>
                            <p class="text-sm text-gray-500">{{ inf.role }}</p>
                            <p class="text-xs text-blue-600 font-bold">{{ inf.social }}</p>
                        </div>
                    </div>
                    <div class="flex gap-1 mb-3">
                        {% for i in range(inf.rating) %}
                        <span class="text-yellow-400">⭐</span>
                        {% endfor %}
                    </div>
                    <p class="text-gray-700 italic leading-relaxed">"{{ inf.review }}"</p>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- MEJORA 12: FAQ Accordion -->
    <section class="py-24 bg-gray-50">
        <div class="container mx-auto px-4 max-w-3xl reveal">
            <h2 class="text-4xl font-bold text-center mb-12">Preguntas Frecuentes</h2>
            {% for faq in data.faqs %}
            <div class="mb-4 bg-white rounded-lg shadow overflow-hidden">
                <button onclick="toggleFAQ({{ loop.index0 }})" class="w-full text-left p-6 font-bold flex justify-between items-center hover:bg-gray-50 transition">
                    <span>{{ faq.q }}</span>
                    <span class="text-2xl transform transition-transform duration-300" id="faq-icon-{{ loop.index0 }}">+</span>
                </button>
                <div id="faq-answer-{{ loop.index0 }}" class="hidden p-6 pt-0 text-gray-600">
                    {{ faq.a }}
                </div>
            </div>
            {% endfor %}
        </div>
    </section>

    <!-- MEJORA 13: Social Media Feed -->
    <section class="py-16 bg-black text-white">
        <div class="container mx-auto px-4 text-center reveal">
            <h3 class="text-2xl font-bold mb-8">Síguenos en redes sociales</h3>
            <div class="flex justify-center gap-8 flex-wrap">
                {% for social in data.social_feed %}
                <div class="text-center">
                    <div class="text-3xl mb-2">
                        {% if social.platform == 'instagram' %}📸
                        {% elif social.platform == 'facebook' %}👍
                        {% else %}🎵{% endif %}
                    </div>
                    <p class="font-bold">{{ social.handle }}</p>
                    <p class="text-sm text-gray-400">{{ social.followers }} seguidores</p>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- MEJORA 14: Newsletter -->
    <section class="py-16 bg-gradient-to-r from-blue-600 to-blue-800 text-white">
        <div class="container mx-auto px-4 text-center reveal">
            <h3 class="text-3xl font-bold mb-4">Únete al Club Calimod</h3>
            <p class="mb-8 text-blue-100">Recibe ofertas exclusivas y contenido premium</p>
            <form class="max-w-md mx-auto flex gap-2" onsubmit="return subscribeNewsletter(event)">
                <input type="email" placeholder="tu@email.com" class="flex-1 px-4 py-3 rounded-lg text-black" required>
                <button type="submit" class="bg-white text-blue-600 px-6 py-3 rounded-lg font-bold hover:bg-gray-100 transition">
                    Suscribirse
                </button>
            </form>
        </div>
    </section>

    <!-- MEJORA 15: Botón flotante WhatsApp mejorado -->
    <a href="https://wa.me/51999999999?text=Hola%20Calimod%2C%20quiero%20más%20información" target="_blank" class="fixed bottom-8 right-8 bg-green-500 text-white p-4 rounded-full shadow-2xl hover:bg-green-600 transition hover:scale-110 z-50 flex items-center justify-center group animate-bounce">
        <span class="absolute right-full mr-4 bg-white text-black text-xs font-bold px-3 py-2 rounded shadow-lg opacity-0 group-hover:opacity-100 transition whitespace-nowrap">¡Consúltanos por WhatsApp!</span>
        <svg class="w-8 h-8 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
    </a>

    <!-- MEJORA 16: Botón "Scroll to Top" -->
    <button id="scroll-top" onclick="scrollToTop()" class="fixed bottom-24 right-8 bg-gray-800 text-white p-3 rounded-full shadow-xl hover:bg-gray-700 transition opacity-0 pointer-events-none z-50">
        ↑
    </button>

    <script>
        // ========== MEJORA 17: Sistema de carga completo ==========
        window.addEventListener('load', () => {
            const loader = document.getElementById('loader');
            setTimeout(() => {
                loader.style.opacity = '0';
                setTimeout(() => { loader.style.display = 'none'; }, 800);
            }, 1500);
        });

        // ========== MEJORA 18: Scroll Reveal mejorado ==========
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                }
            });
        }, { threshold: 0.1 });
        document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

        // Cursor Follower
        const cursor = document.getElementById('cursor');
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        // ========== MEJORA 19: Navegación del carrusel funcional ==========
        function scrollCarousel(direction) {
            const container = document.getElementById('carousel-container');
            const scrollAmount = 350; // Ancho de cada tarjeta + gap
            if (direction === 'left') {
                container.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
            } else {
                container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
            }
        }

        // ========== MEJORA 20: Modal de video funcional ==========
        function openVideoModal(videoSrc) {
            const modal = document.getElementById('video-modal');
            const video = document.getElementById('modal-video');
            video.querySelector('source').src = videoSrc;
            video.load();
            modal.classList.add('active');
        }

        function closeVideoModal() {
            const modal = document.getElementById('video-modal');
            const video = document.getElementById('modal-video');
            video.pause();
            modal.classList.remove('active');
        }

        // Cerrar modal al hacer clic fuera del video
        document.getElementById('video-modal').addEventListener('click', (e) => {
            if (e.target.id === 'video-modal') {
                closeVideoModal();
            }
        });

        // ========== MEJORA 21: Toggle FAQ ==========
        function toggleFAQ(index) {
            const answer = document.getElementById(`faq-answer-${index}`);
            const icon = document.getElementById(`faq-icon-${index}`);
            
            if (answer.classList.contains('hidden')) {
                answer.classList.remove('hidden');
                icon.textContent = '−';
                icon.style.transform = 'rotate(180deg)';
            } else {
                answer.classList.add('hidden');
                icon.textContent = '+';
                icon.style.transform = 'rotate(0deg)';
            }
        }

        // ========== MEJORA 22: Scroll to products ==========
        function scrollToProducts() {
            document.getElementById('productos').scrollIntoView({ behavior: 'smooth' });
        }

        // ========== MEJORA 23: Newsletter subscription ==========
        function subscribeNewsletter(event) {
            event.preventDefault();
            const email = event.target.querySelector('input[type="email"]').value;
            alert(`¡Gracias por suscribirte! Pronto recibirás nuestras ofertas en ${email}`);
            event.target.reset();
            return false;
        }

        // ========== MEJORA 24: Scroll to top button ==========
        const scrollTopBtn = document.getElementById('scroll-top');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 500) {
                scrollTopBtn.style.opacity = '1';
                scrollTopBtn.style.pointerEvents = 'auto';
            } else {
                scrollTopBtn.style.opacity = '0';
                scrollTopBtn.style.pointerEvents = 'none';
            }
        });

        function scrollToTop() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // ========== MEJORA 25: Show slide detail ==========
        function showSlideDetail(index) {
            const slides = [
                {
                    title: "Innovando desde el inicio",
                    content: "En 1980, Calimod abrió su primera planta en Ate, Lima. Desde entonces, hemos mantenido nuestra tradición de excelencia en la fabricación de calzado de cuero premium, combinando técnicas artesanales con tecnología moderna."
                },
                {
                    title: "Tecnología Flexible",
                    content: "Nuestras suelas con tecnología Memory Foam se adaptan perfectamente a tu pisada, ofreciendo comodidad durante todo el día. El material flexible recupera su forma original después de cada uso."
                },
                {
                    title: "Ultralight + Memory Foam",
                    content: "Sistema de doble densidad que combina EVA ultraligero con plantillas de memory foam. El resultado: 40% más ligero que el calzado tradicional de cuero, sin comprometer la durabilidad."
                },
                {
                    title: "Camina la historia",
                    content: "Diseñado para profesionales modernos que necesitan calzado versátil. Ideal para oficina, reuniones y eventos sociales. Resistente a jornadas de más de 12 horas sin sacrificar estilo."
                }
            ];
            
            alert(`${slides[index].title}\n\n${slides[index].content}`);
        }

        // Lógica del Zapato
        const shoe = document.getElementById('shoe-btn');
        const hint = document.getElementById('finger-hint');
        const successBox = document.getElementById('success-box');
        
        function bendShoe() {
            shoe.classList.add('bend-active');
            hint.style.display = 'none';
        }
        
        function releaseShoe() {
            shoe.classList.remove('bend-active');
            setTimeout(() => {
                successBox.classList.remove('hidden');
                successBox.classList.remove('translate-y-4', 'opacity-0');
            }, 300);
        }

        // ========== MEJORA 26: Analytics tracking simulation ==========
        document.querySelectorAll('button').forEach(btn => {
            btn.addEventListener('click', () => {
                console.log('Event tracked:', btn.textContent.trim());
            });
        });

        // ========== MEJORA 27: Lazy loading optimization ==========
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.src) {
                            img.src = img.dataset.src;
                            img.removeAttribute('data-src');
                        }
                        imageObserver.unobserve(img);
                    }
                });
            });
            
            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        }

        // ========== MEJORA 36: Navbar scroll effect ==========
        window.addEventListener('scroll', () => {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 100) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // ========== MEJORA 37: Countdown timer (ejemplo) ==========
        function startCountdown() {
            const countdownDate = new Date().getTime() + (24 * 60 * 60 * 1000); // 24 horas
            
            const timer = setInterval(() => {
                const now = new Date().getTime();
                const distance = countdownDate - now;
                
                const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((distance % (1000 * 60)) / 1000);
                
                console.log(`Oferta termina en: ${hours}h ${minutes}m ${seconds}s`);
                
                if (distance < 0) {
                    clearInterval(timer);
                }
            }, 1000);
        }
        // startCountdown(); // Descomentar para activar

        // ========== MEJORA 38: Keyboard navigation ==========
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeVideoModal();
            }
            if (e.key === 'ArrowLeft') {
                scrollCarousel('left');
            }
            if (e.key === 'ArrowRight') {
                scrollCarousel('right');
            }
        });

        // ========== MEJORA 39: Performance monitoring ==========
        window.addEventListener('load', () => {
            if ('performance' in window) {
                const perfData = performance.timing;
                const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
                console.log(`Página cargada en: ${pageLoadTime}ms`);
            }
        });

        // ========== MEJORA 40: Auto-save form data ==========
        const emailInput = document.querySelector('input[type="email"]');
        if (emailInput) {
            emailInput.addEventListener('input', (e) => {
                localStorage.setItem('savedEmail', e.target.value);
            });
            
            // Recuperar email guardado
            const savedEmail = localStorage.getItem('savedEmail');
            if (savedEmail) {
                emailInput.value = savedEmail;
            }
        }

        // ========== MEJORA 41: Share functionality ==========
        async function shareContent() {
            if (navigator.share) {
                try {
                    await navigator.share({
                        title: 'Calimod - Legado en Movimiento',
                        text: 'Descubre la nueva colección de zapatos con tecnología Ultralight',
                        url: window.location.href
                    });
                } catch (err) {
                    console.log('Error sharing:', err);
                }
            }
        }

        // ========== MEJORA 42: Print functionality ==========
        function printPage() {
            window.print();
        }

        // ========== MEJORA 43: Dark mode toggle (opcional) ==========
        function toggleDarkMode() {
            document.body.classList.toggle('dark-mode');
            localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
        }

        // Recuperar preferencia de dark mode
        if (localStorage.getItem('darkMode') === 'true') {
            document.body.classList.add('dark-mode');
        }

        // ========== MEJORA 44: Cookie consent (simulado) ==========
        window.addEventListener('load', () => {
            const cookieConsent = localStorage.getItem('cookieConsent');
            if (!cookieConsent) {
                setTimeout(() => {
                    const accept = confirm('Este sitio usa cookies para mejorar tu experiencia. ¿Aceptas?');
                    if (accept) {
                        localStorage.setItem('cookieConsent', 'true');
                    }
                }, 2000);
            }
        });

        // ========== MEJORA 45: Error handling para imágenes ==========
        document.querySelectorAll('img').forEach(img => {
            img.addEventListener('error', function() {
                this.src = 'https://via.placeholder.com/400x300/cccccc/666666?text=Imagen+no+disponible';
                this.alt = 'Imagen no disponible';
            });
        });

        console.log('✅ Todas las mejoras cargadas correctamente');
        console.log('🚀 Campaña Digital Calimod - Versión Mejorada v2.0');
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_code, data=campaign)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')