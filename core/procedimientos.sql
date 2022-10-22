CREATE or REPLACE procedure sp_listar_personas(personas out SYS_REFCURSOR)

IS
BEGIN 

    open personas for select * from core_persona;

END;


create or replace procedure sp_listar_comunas(comunas out SYS_REFCURSOR)

IS
BEGIN

    open comunas for SELECT * from core_comuna;

end;



create or replace procedure sp_agregar_persona(
    v_rut varchar2,
    v_nombre varchar2,
    v_apellido varchar2,
    v_fecha date,
    v_direccion varchar2,
    v_comuna_id number,
    v_salida out number
)

IS
begin  

    insert into core_persona(rut, nombre, apellido, fecha_nacimiento, direccion, comuna_id)
    values(v_rut, v_nombre, v_apellido, v_fecha, v_direccion, v_comuna_id);
    commit;

    v_salida: =1;

    exception

    when others THEN
        v_salida: =0;


end;
    