CREATE TRIGGER add_recebimento AFTER insert
ON sistema_pedidos_loja
BEGIN
  INSERT INTO sistema_pedidos_recebimento ('loja_id', 'nome', 'situacao') VALUES (NEW.id, 'Balcao', 1);
  INSERT INTO sistema_pedidos_recebimento ('loja_id', 'nome', 'situacao') VALUES (NEW.id, 'Mesa', 0);
  INSERT INTO sistema_pedidos_recebimento ('loja_id', 'nome', 'situacao') VALUES (NEW.id, 'Carro', 0);
END;
