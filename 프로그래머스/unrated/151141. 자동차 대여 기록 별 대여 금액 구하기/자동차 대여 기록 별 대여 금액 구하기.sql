-- 코드를 입력하세요
SELECT HISTORY_ID, 
       ROUND((DAILY_FEE * (DATEDIFF(END_DATE, START_DATE) + 1) * (100 - IFNULL(DISCOUNT_RATE, 0))/100), 0) AS FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
JOIN CAR_RENTAL_COMPANY_CAR AS C
ON H.CAR_ID = C.CAR_ID AND C.CAR_TYPE = '트럭'
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P
ON C.CAR_TYPE = P.CAR_TYPE
AND P.DURATION_TYPE = ( CASE WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 90 THEN '90일 이상'
                             WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '30일 이상'
                             WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 7 THEN '7일 이상'
                             ELSE NULL
                        END )
ORDER BY FEE DESC, HISTORY_ID DESC;