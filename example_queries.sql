-- INTERSECTS
SELECT ST_Intersects(
               ST_SetSRID(ST_MakePoint(-79.99701625706184, 40.444975822624855), 4326),
               geom
       )
FROM public.pit_neighborhoods;

SELECT *
FROM public.pit_neighborhoods
WHERE ST_Intersects(
              ST_SetSRID(ST_MakePoint(-79.99701625706184, 40.444975822624855), 4326),
              geom
      )
;
-- MAKE POINT
SELECT ST_makepoint(-79.99701625706184, 40.444975822624855);
SELECT ST_SRID(ST_makepoint(-79.99701625706184, 40.444975822624855));
SELECT st_setsrid(ST_makepoint(-79.99701625706184, 40.444975822624855), 4326);
SELECT ST_SRID(ST_SetSRID(ST_makepoint(-79.99701625706184, 40.444975822624855), 4326));
-- MAKE POINT AS TEXT
SELECT st_astext(ST_makepoint(-79.99701625706184, 40.444975822624855));

-- Transform
SELECT ST_SetSRID(ST_MakePoint(-79.99701625706184, 40.444975822624855), 4326);
SELECT ST_SRID(ST_SetSRID(ST_MakePoint(-79.99701625706184, 40.444975822624855), 4326));
SELECT ST_Transform(ST_SetSRID(ST_MakePoint(-79.99701625706184, 40.444975822624855), 4326), 3857);
SELECT ST_SRID(ST_Transform(ST_SetSRID(ST_MakePoint(-79.99701625706184, 40.444975822624855), 4326), 3857));

-- Contains
SELECT ST_Contains(
               ST_SetSRID(ST_MakePoint(-79.99701625706184, 40.444975822624855), 4326),
               geom
       )
FROM public.pit_neighborhoods;
-- THESE ARE NOT THE SAME
SELECT ST_Contains(
               geom,
               ST_SetSRID(ST_MakePoint(-79.99701625706184, 40.444975822624855), 4326)
       )
FROM public.pit_neighborhoods;

-- Distance
-- Cast as geography to get meters
SELECT geom,
       ST_SetSRID(ST_MakePoint(-79.99701625706184, 40.444975822624855), 4326)::geography,
       ST_Distance(
               ST_SetSRID(ST_MakePoint(-79.99701625706184, 40.444975822624855), 4326)::geography,
               geom::geography
       )
FROM public.pit_neighborhoods;