SELECT customers.firstname, customers.lastname, customers.city FROM customers
JOIN employees ON supportrepid=employeeid


WHERE customers.city = (SELECT city FROM employees WHERE reportsto IS NULL)
