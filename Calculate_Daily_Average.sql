use Speed_DB;
SELECT 
    DATE(TestDate) AS 'Test Date',
    ISP,
    FORMAT(MAX(Download), 2) AS 'Download Max',
    FORMAT(MIN(Download), 2) AS 'Download Min',
    FORMAT(AVG(Download), 2) AS 'Download Average',
    FORMAT(MAX(Upload), 2) AS 'Upload Max',
    FORMAT(MIN(Upload), 2) AS 'Upload Min',
    FORMAT(AVG(Upload), 2) AS 'Upload Average'
FROM
    Tests
WHERE
    ISP = 'Spectrum'
GROUP BY DATE(TestDate);