import boto3
from datetime import datetime, UTC
from dateutil.relativedelta import relativedelta

def get_cost_client():
    return boto3.client('ce', region_name='us-east-1')

def get_current_month_dates():
    now = datetime.now(UTC)
    start = now.replace(day=1).strftime('%Y-%m-%d')
    end = now.strftime('%Y-%m-%d')
    return start, end

def get_monthly_summary():
    client = get_cost_client()
    start, end = get_current_month_dates()

    try: 
        response = client.get_cost_and_usage(
            TimePeriod= {'Start': start, 'End': end},
            Granularity= 'MONTHLY',
            Metrics=['UnblendedCost']

        )
    except Exception as e: 
        raise Exception(f"Failed to fetch cost data: {str(e)}")

    
    result = response['ResultsByTime'][0]
    amount = float(result['Total']['UnblendedCost']['Amount'])
    unit = result['Total']['UnblendedCost']['Unit']

    return {
        "period": f"{start} to {end}",
        "total_cost": round(amount, 2),
        "unit": unit
    }


def get_cost_breakdown():
    client = get_cost_client()
    start, end = get_current_month_dates()

    try: 
    
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': start,
                'End': end
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost'],
           GroupBy=[
               {
                   'Type': 'DIMENSION',
                   'Key': 'SERVICE'
               } 
           ]
      )

    except Exception as e:
      raise Exception(f"Failed to fetch Cost breakdown: {str(e)}")

    results = response['ResultsByTime'][0]['Groups']

    breakdown = []
    for item in results:
        service = item['Keys'][0]
        amount = float(item['Metrics']['UnblendedCost']['Amount'])
        if amount > 0:
            breakdown.append({
                "service": service,
                "cost": round(amount ,4),
                "unit": "USD"
            })

    breakdown.sort(key=lambda x: x['cost'], reverse=True)

    return {
        "period": f"{start} to {end}",
        "breakdown": breakdown
    }


def get_cost_history():
    client = get_cost_client()
    start, end = get_current_month_dates()


    try: 

        response = client.get_cost_and_usage(
         TimePeriod ={
            'Start': start,
            'End': end
         },


         Granularity= 'DAILY',
         Metrics= ['UnblendedCost']

     )

    except Exception as e:
     raise Exception(f"Failed to fetch Cost History: {str(e)}")

    results = response['ResultsByTime']

    daily_costs = []
    

    for item in results: 
      date = item['TimePeriod']['Start']
      amount = float(item['Total']['UnblendedCost']['Amount'])
      daily_costs.append({
        "date": date,
        "cost": round(amount ,4),
      })

      

    return {
        "period": f"{start} to {end}",
        "daily_costs": daily_costs
    }

    