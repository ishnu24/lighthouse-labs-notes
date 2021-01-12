SELECT firstname, lastname FROM employees WHERE employeeid = 
(SELECT reportsto FROM employees WHERE employeeid IN (SELECT customers.supportrepid FROM customers WHERE country = 'Brazil'))
