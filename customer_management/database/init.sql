CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    contact TEXT NOT NULL,
    country TEXT NOT NULL,
    state TEXT,
    city TEXT NOT NULL,
    neighborhood TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT OR IGNORE INTO customers (name, email, contact, country, state, city, neighborhood, created_at)
VALUES ('João Silva', 'joao.silva@email.com', '+5511999999999', 'Brasil', 'São Paulo', 'São Paulo', 'Vila Mariana', '2024-01-01');

INSERT OR IGNORE INTO customers (name, email, contact, country, state, city, neighborhood, created_at)
VALUES ('Maria Santos', 'maria.santos@email.com', '+5511988888888', 'Brasil', 'São Paulo', 'São Paulo', 'Moema', '2024-01-01');

INSERT OR IGNORE INTO customers (name, email, contact, country, state, city, neighborhood, created_at)
VALUES ('Pedro Oliveira', 'pedro.oliveira@email.com', '+5511977777777', 'Brasil', 'Rio de Janeiro', 'Rio de Janeiro', 'Copacabana', '2024-01-01');

INSERT OR IGNORE INTO customers (name, email, contact, country, state, city, neighborhood, created_at)
VALUES ('Ana Souza', 'ana.souza@email.com', '+351123456789', 'Portugal', 'Lisboa', 'Lisboa', 'Baixa', '2024-01-01');

INSERT OR IGNORE INTO customers (name, email, contact, country, state, city, neighborhood, created_at)
VALUES ('Manuel Torres', 'manuel.torres@email.com', '+351987654321', 'Portugal', 'Porto', 'Porto', 'Ribeira', '2024-01-01');

INSERT INTO customers (name, email, contact, country, state, city, neighborhood, created_at) VALUES 
-- January
('Carlos Rodriguez', 'carlos.r@email.com', '+34666555444', 'Espanha', 'Madrid', 'Madrid', 'Centro', '2024-02-01'),
('Isabella Ferrari', 'isabella.f@email.com', '+39333222111', 'Itália', 'Roma', 'Roma', 'Centro Storico', '2024-02-01'),
('Hans Schmidt', 'hans.s@email.com', '+49123456789', 'Alemanha', 'Berlim', 'Berlim', 'Mitte', '2024-02-15'),
('Sophie Martin', 'sophie.m@email.com', '+33123456789', 'França', 'Paris', 'Paris', 'Le Marais', '2024-02-15'),
('John Smith', 'john.s@email.com', '+44123456789', 'Reino Unido', 'Londres', 'Londres', 'Westminster', '2024-02-28'),

-- March
('Lucas Costa', 'lucas.c@email.com', '+5511944444444', 'Brasil', 'São Paulo', 'Campinas', 'Centro', '2024-03-01'),
('Beatriz Lima', 'beatriz.l@email.com', '+5511933333333', 'Brasil', 'São Paulo', 'Santos', 'Gonzaga', '2024-03-01'),
('Ricardo Santos', 'ricardo.s@email.com', '+5521922222222', 'Brasil', 'Rio de Janeiro', 'Niterói', 'Icaraí', '2024-03-15'),
('Emma Wilson', 'emma.w@email.com', '+44789123456', 'Reino Unido', 'Inglaterra', 'Manchester', 'Centro', '2024-03-15'),
('Luis Garcia', 'luis.g@email.com', '+34611222333', 'Espanha', 'Barcelona', 'Barcelona', 'Eixample', '2024-03-15'),

-- April
('Antonio Ferrari', 'antonio.f@email.com', '+39345678901', 'Itália', 'Milão', 'Milão', 'Brera', '2024-04-01'),
('Marie Dubois', 'marie.d@email.com', '+33234567890', 'França', 'Lyon', 'Lyon', 'Presqu''île', '2024-04-01'),
('Thomas Weber', 'thomas.w@email.com', '+49234567890', 'Alemanha', 'Munique', 'Munique', 'Altstadt', '2024-04-15'),
('Ana Torres', 'ana.t@email.com', '+351234567890', 'Portugal', 'Porto', 'Porto', 'Ribeira', '2024-04-15'),
('James Brown', 'james.b@email.com', '+44234567890', 'Reino Unido', 'Londres', 'Londres', 'Shoreditch', '2024-04-30'),

-- May
('Paulo Ferreira', 'paulo.f@email.com', '+5511955555555', 'Brasil', 'São Paulo', 'São Paulo', 'Pinheiros', '2024-05-01'),
('Carmen Rodriguez', 'carmen.r@email.com', '+34633444555', 'Espanha', 'Madrid', 'Madrid', 'Salamanca', '2024-05-01'),
('Giuseppe Rossi', 'giuseppe.r@email.com', '+39345678902', 'Itália', 'Roma', 'Roma', 'Trastevere', '2024-05-15'),
('Pierre Martin', 'pierre.m@email.com', '+33345678901', 'França', 'Paris', 'Paris', 'Montmartre', '2024-05-15'),
('Sarah Johnson', 'sarah.j@email.com', '+44345678901', 'Reino Unido', 'Londres', 'Londres', 'Notting Hill', '2024-05-30'),

-- June
('Laura Fernandes', 'laura.f@email.com', '+5511966666666', 'Brasil', 'São Paulo', 'São Paulo', 'Itaim Bibi', '2024-06-01'),
('Miguel Santos', 'miguel.s@email.com', '+351345678901', 'Portugal', 'Lisboa', 'Lisboa', 'Chiado', '2024-06-01'),
('Elena Martinez', 'elena.m@email.com', '+34644555666', 'Espanha', 'Barcelona', 'Barcelona', 'Gracia', '2024-06-15'),
('Marco Rossi', 'marco.r@email.com', '+39345678903', 'Itália', 'Florença', 'Florença', 'Centro', '2024-06-15'),
('Alice Martin', 'alice.m@email.com', '+33456789012', 'França', 'Marselha', 'Marselha', 'Vieux-Port', '2024-06-30'),

-- July
('Rafael Costa', 'rafael.c@email.com', '+5511977777777', 'Brasil', 'Rio de Janeiro', 'Rio de Janeiro', 'Leblon', '2024-07-01'),
('Sofia Almeida', 'sofia.a@email.com', '+351456789012', 'Portugal', 'Porto', 'Porto', 'Foz', '2024-07-01'),
('Pablo Garcia', 'pablo.g@email.com', '+34655666777', 'Espanha', 'Madrid', 'Madrid', 'Retiro', '2024-07-15'),
('Lucia Ferrari', 'lucia.f@email.com', '+39345678904', 'Itália', 'Veneza', 'Veneza', 'San Marco', '2024-07-15'),
('Henri Dubois', 'henri.d@email.com', '+33567890123', 'França', 'Nice', 'Nice', 'Vieux Nice', '2024-07-30'),

-- August
('Carla Santos', 'carla.s@email.com', '+5511988888888', 'Brasil', 'São Paulo', 'São Paulo', 'Jardins', '2024-08-01'),
('Tiago Silva', 'tiago.s@email.com', '+351567890123', 'Portugal', 'Lisboa', 'Lisboa', 'Alfama', '2024-08-01'),
('Ana Rodriguez', 'ana.r@email.com', '+34666777888', 'Espanha', 'Sevilha', 'Sevilha', 'Santa Cruz', '2024-08-15'),
('Paolo Conti', 'paolo.c@email.com', '+39345678905', 'Itália', 'Milão', 'Milão', 'Navigli', '2024-08-15'),
('Claire Martin', 'claire.m@email.com', '+33678901234', 'França', 'Lyon', 'Lyon', 'Vieux Lyon', '2024-08-30'),

-- September
('Bruno Oliveira', 'bruno.o@email.com', '+5511999999999', 'Brasil', 'São Paulo', 'Campinas', 'Cambuí', '2024-09-01'),
('Mariana Costa', 'mariana.c@email.com', '+351678901234', 'Portugal', 'Porto', 'Porto', 'Boavista', '2024-09-01'),
('Diego Torres', 'diego.t@email.com', '+34677888999', 'Espanha', 'Valencia', 'Valencia', 'El Carmen', '2024-09-15'),
('Valentina Ricci', 'valentina.r@email.com', '+39345678906', 'Itália', 'Roma', 'Roma', 'Monti', '2024-09-15'),
('Louis Bernard', 'louis.b@email.com', '+33789012345', 'França', 'Paris', 'Paris', 'Marais', '2024-09-30'),

-- October
('Felipe Santos', 'felipe.s@email.com', '+5521912345678', 'Brasil', 'Rio de Janeiro', 'Rio de Janeiro', 'Ipanema', '2024-10-01'),
('Beatriz Ferreira', 'beatriz.f@email.com', '+351789012345', 'Portugal', 'Lisboa', 'Lisboa', 'Belém', '2024-10-01'),
('Javier Lopez', 'javier.l@email.com', '+34688999000', 'Espanha', 'Barcelona', 'Barcelona', 'Barceloneta', '2024-10-15'),
('Chiara Romano', 'chiara.r@email.com', '+39345678907', 'Itália', 'Florença', 'Florença', 'Santa Croce', '2024-10-15'),
('Marie Laurent', 'marie.l@email.com', '+33890123456', 'França', 'Bordeaux', 'Bordeaux', 'Saint-Pierre', '2024-10-30'),

-- November
('Ramon Garcia', 'ramon.g@email.com', '+34699000111', 'Espanha', 'Madrid', 'Madrid', 'La Latina', '2024-11-15'),
('Andrea Marino', 'andrea.m@email.com', '+39345678908', 'Itália', 'Veneza', 'Veneza', 'Dorsoduro', '2024-11-15'),
('Sophie Petit', 'sophie.p@email.com', '+33901234567', 'França', 'Lyon', 'Lyon', 'Croix-Rousse', '2024-11-30'),

-- December
('Gabriel Costa', 'gabriel.c@email.com', '+5511934567890', 'Brasil', 'São Paulo', 'São Paulo', 'Moema', '2024-12-01'),
('Inês Silva', 'ines.s@email.com', '+351901234567', 'Portugal', 'Lisboa', 'Lisboa', 'Príncipe Real', '2024-12-01'),
('Carlos Moreno', 'carlos.m@email.com', '+34600111222', 'Espanha', 'Barcelona', 'Barcelona', 'Poblenou', '2024-12-15'),
('Francesca Longo', 'francesca.l@email.com', '+39345678909', 'Itália', 'Roma', 'Roma', 'Testaccio', '2024-12-15'),
('Jean Dupont', 'jean.d@email.com', '+33012345678', 'França', 'Paris', 'Paris', 'Bastille', '2024-12-30'); 