from datetime import date

dmd_data = {
    'og_ct': 3000,
    'launch_dt': date(2014, 6, 30),
    'prev_wk': 230,
    'inv': 2000,
    'og_p': 85.99,
    'crrnt_p': 52.59
}


def get_age(launch_dt=dmd_data['launch_dt']):
    ###Number of days between launch and current date###
    assert isinstance(launch_dt, date), "Date Exception"
    dt_diff = (date.today()-launch_dt).days
    return dt_diff


def wk_demand(og_ct=dmd_data['og_ct'], launch_dt=dmd_data['launch_dt'],
              prev_wk=dmd_data['prev_wk'], inv=dmd_data['inv'],
              og_p=dmd_data['og_p'], crrnt_p=dmd_data['crrnt_p']):

    ### Demand Regresiion.  Replace with Statsmodel ####

    age = get_age(launch_dt)
    dsct_p = og_p/crrnt_p
    demand_w = .2*og_ct+200/age+.8*prev_wk+.15*inv+10*dsct_p
    return demand_w
