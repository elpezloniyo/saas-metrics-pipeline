with subscriptions as (
    select * from {{ ref('stg_subscriptions') }}
)

select
    subscription_id,
    customer_id,
    plan_name,
    status,
    mrr_amount,
    (mrr_amount * 12) as arr_amount,
    created_at,
    canceled_at,
    case 
        when status = 'canceled' then true 
        else false 
    end as is_churned
from subscriptions
