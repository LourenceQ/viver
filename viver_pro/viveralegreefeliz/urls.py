from django.urls import path
from .import views

app_name = "viveralegreefeliz"

urlpatterns = [
    path('',views.index, name='index'),
    path('aconselhamento/',views.aconselhamento, name='aconselhamento'),
    path('agua_magnetizada_saude/',views.agua_magnetizada_saude, name='agua_magnetizada_saude'),
    path('agua_magnetizada/',views.agua_magnetizada, name='agua_magnetizada'),
    path('arteterapia/',views.arteterapia, name='arteterapia'),
    path('constelacao_familiar/',views.constelacao_familiar, name='constelacao_familiar'), #
    path('desenvolvimento_pessoal/',views.desenvolvimento_pessoal, name='desenvolvimento_pessoal'),
    path('galeria',views.galeria, name='galeria'),
    path('introducao_constelacao_familiar/',views.introducao_constelacao_familiar, name='introducao_constelacao_familiar'),#
    path('loja/',views.loja, name='loja'),
    path('mandalas/',views.mandalas, name='mandalas'),
    path('meditacao_mentalizacao/',views.meditacao_mentalizacao, name='meditacao_mentalizacao'),
    path('pnl/',views.pnl, name='pnl'),
    path('quemsomos/',views.quemsomos, name='quemsomos'),
    path('agendar/',views.agendar,name='agendar'),
    path('terapias_integrativas/',views.terapias_integrativas,name='terapias_integrativas')

]
