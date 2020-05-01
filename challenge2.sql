
-- * Assume table `employee` contains employees who do not have any subordinates
-- * and table `manager` contains employees who have subordinates;
-- * In table `table_1`, if a record has NaN value in the `id_manager` filed, it means that
-- * this employee doesn't have any superiors/ managers.

select first_name, last_name
from table_1, (select * from employee
        union (select id_manager as id_employee, first_name, last_name from manager)) as all_employees
where table_1.id_employee = all_employees.id_employee
    and dt_work_from <= "2020-01-01"
    and dt_work_to >= "2020-01-31"