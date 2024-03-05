from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="example_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag:
    bash_t1 = BashOperator(
        dag_id = 'bash_t1',
        bash_command="echo whoiam"
    )
    bash_t2 = BashOperator(
        dag_id = 'bash_t2',
        bash_command="echo $HOSTNAME"
    )
# [END howto_operator_bash_skip]
bash_t1 >> bash_t2