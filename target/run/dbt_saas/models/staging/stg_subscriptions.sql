
  create view "saas_analytics"."analytics_staging"."stg_subscriptions__dbt_tmp"
    
    
  as (
    with source as (
    select * from "saas_analytics"."raw"."raw_subscriptions"
),

renamed as (
    select
        subscription_id,
        customer_id,
        plan_name,
        cast(mrr_amount as numeric(10,2)) as mrr_amount,
        currency,
        status,
        cast(created_at as timestamp) as created_at,
        cast(canceled_at as timestamp) as canceled_at
    from source
)

select * from renamed
  );