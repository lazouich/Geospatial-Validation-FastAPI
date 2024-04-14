shp2pgsql \
   -c \
  -D \
  -I \
  -s 4326 \
  geospatial_datasets/Neighborhoods_PIT/Neighborhoods_ \
  public.pit_neighborhoods \
  | psql -d postgres -U postgres



shp2pgsql \
   -c \
  -D \
  -I \
  -s 4326 \
  geospatial_datasets/US_State_boundaries/cb_2018_us_state_500k.shp \
  public.us_boundary \
  | psql -d postgres -U postgres
