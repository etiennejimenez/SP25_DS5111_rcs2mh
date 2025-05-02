{{ config(materialized='table') }}

SELECT EN,DE
FROM DATA_SCIENCE.RCS2MH_RAW.NUMBERS
