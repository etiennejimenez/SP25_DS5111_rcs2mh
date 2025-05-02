{{ config(materialized='table') }}

SELECT EN,FR
FROM DATA_SCIENCE.RCS2MH_RAW.NUMBERS
