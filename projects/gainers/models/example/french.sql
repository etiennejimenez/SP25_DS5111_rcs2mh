{{ config(materialized='table') }}

SELECT FR
FROM DATA_SCIENCE.RCS2MH_RAW.NUMBERS
