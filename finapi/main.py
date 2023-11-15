from fastapi import FastAPI
from .routes import auth_router
from .routes import users_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/user/me", tags=["user_me"])
# app.include_router(bank_account_router, prefix="/bank_account_types", tags=["bank_account_types"])
# app.include_router(crypto_chains_router, prefix="/crypto_chains", tags=["crypto_chains"])
# app.include_router(currencies_router, prefix="/currencies", tags=["currencies"])
# app.include_router(generic_asset_categories_router, prefix="/generic_asset_categories", tags=["generic_asset_categories"])
# app.include_router(institutions_router, prefix="/institutions_router", tags=["institutions_router"])
# app.include_router(precious_metals_router, prefix="/precious_metals", tags=["precious_metals"])
# app.include_router(real_estates_router, prefix="/real_estates", tags=["real_estates"])
# app.include_router(scpis_router, prefix="/scpis", tags=["scpis"])
# app.include_router(securities_router, prefix="/securities", tags=["securities"])
# app.include_router(watches_router, prefix="/watches", tags=["watches"])
