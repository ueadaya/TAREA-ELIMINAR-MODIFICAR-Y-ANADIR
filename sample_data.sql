USE desarrollo_web;

-- Productos
INSERT INTO productos (nombre, precio, stock) VALUES
('Laptop HP', 750.00, 15),
('Mouse Logitech', 25.50, 100),
('Teclado Mecánico', 45.99, 50),
('Monitor Samsung 24"', 180.00, 30),
('Impresora Epson', 120.00, 20),
('Silla Ergonómica', 85.00, 40),
('Escritorio Oficina', 150.00, 25),
('Disco Duro 1TB', 60.00, 70),
('Memoria USB 32GB', 12.00, 200),
('Auriculares Sony', 35.00, 60);

-- Clientes
INSERT INTO clientes (nombre, apellido, correo, telefono) VALUES
('Juan', 'Pérez', 'juan.perez@gmail.com', '0991234567'),
('María', 'López', 'maria.lopez@gmail.com', '0987654321'),
('Carlos', 'Gómez', 'carlos.gomez@gmail.com', '0971122334'),
('Ana', 'Torres', 'ana.torres@gmail.com', '0969988776'),
('Pedro', 'Ramírez', 'pedro.ramirez@gmail.com', '0955566778');

-- Facturas
INSERT INTO facturas (numero_factura, fecha, id_cliente) VALUES
('FAC-001', '2025-09-01', 1),
('FAC-002', '2025-09-02', 2),
('FAC-003', '2025-09-03', 3),
('FAC-004', '2025-09-04', 4),
('FAC-005', '2025-09-05', 5);

-- Detalles de Facturas
INSERT INTO detalle_factura (id_factura, id_producto, cantidad, subtotal) VALUES
(1, 1, 1, 750.00),
(1, 2, 2, 51.00),
(2, 3, 1, 45.99),
(2, 4, 2, 360.00),
(3, 5, 1, 120.00),
(3, 6, 1, 85.00),
(4, 7, 1, 150.00),
(4, 8, 2, 120.00),
(5, 9, 5, 60.00),
(5, 10, 1, 35.00);

-- Inventario
INSERT INTO inventario (id_producto, cantidad, tipo_movimiento) VALUES
(1, 15, 'entrada'),
(2, 100, 'entrada'),
(3, 50, 'entrada'),
(4, 30, 'entrada'),
(5, 20, 'entrada');
