use Speed_DB;
drop table Summary;
create table Summary(
    TestDate date,
    IPS varchar(20),
    Download_Max float,
    Download_Min float,
    Download_Avg float,
    Upload_Max float,
    Upload_Min float,
    Upload_Avg float);