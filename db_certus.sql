create database bd_certus;

use bd_certus;

select * from t_estudiantes;

-- Crea la tabla "knowledge" para almacenar preguntas y respuestas
CREATE TABLE knowledge (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT,
    answer TEXT
);

-- Insertar algunas preguntas y respuestas de ejemplo
INSERT INTO knowledge (question, answer) VALUES
	("Hola", "Hola soy el chatbot de certus"),
    ("Como estas", "Estoy bien y tu?"),
    ("bien", " Me alegro por ti"),
    ("mal", "¿Qué puedo hacer para ayudarte?"),
    ("¿Cuáles son los requisitos para el curso?", "Saber programación y matemáticas."),
    ("¿Qué temas se tratan en el curso?", "Aprendizaje automático y redes neuronales."),
    ("proyecto final", "Sí, es crear un chatgtp");
    
INSERT INTO knowledge (question, answer)
VALUES
    ('Clima hoy', 'No tengo información sobre el clima.'),
    ('Aprender programación', 'Comienza con Python y busca tutoriales en línea.'),
    ('Inteligencia artificial', 'Campo de la informática que simula la inteligencia humana.'),
    ('Capital de Francia', 'París.'),
    ('PNL', 'Enfoque de comunicación y desarrollo personal.'),
    ('Aprendizaje automático', 'Rama de la inteligencia artificial que usa datos para aprender.'),
    ('Mejorar habilidades de programación', 'Practica, trabaja en proyectos y estudia código.'),
    ('Lenguaje de programación recomendado', 'Python es un buen punto de partida.'),
    ('Diferencia entre inteligencia artificial y aprendizaje automático', 'IA vs. técnica específica de IA.'),
    ('Futuro de la inteligencia artificial', 'Juega un papel en muchas industrias en constante evolución.');

INSERT INTO knowledge (question, answer)
VALUES
    ('Temas en el curso IA', 'Aprendizaje automático, visión por computadora, NLP, redes neuronales.'),
    ('Nivel de dificultad IA', 'Intermedio a avanzado, conocimientos de programación y matemáticas requeridos.'),
    ('Duración del curso IA', 'Aproximadamente 12 semanas.'),
    ('Experiencia previa requerida IA', 'No es necesaria, conocimientos básicos son útiles.'),
    ('Recursos de aprendizaje IA', 'Conferencias, tutoriales en línea y proyectos prácticos.'),
    ('Certificación curso IA', 'Sí, se emite una certificación al completar el curso.'),
    ('Enfoque del curso IA', 'Desarrollar aplicaciones de IA con herramientas modernas.'),
    ('Proyecto final curso IA', 'Sí, requerido para demostrar comprensión.'),
    ('Costo curso IA', 'Varía según la institución, verifica en su sitio web.'),
    ('Información adicional IA', 'Visita el sitio web de la institución para más detalles.');
    
    

select * from knowledge;