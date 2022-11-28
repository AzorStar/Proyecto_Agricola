import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './components/app/app.component';
import { HeaderComponent } from './components/header/header.component';
import { VentasComponent } from './components/ventas/ventas.component';
import { DistribucionComponent } from './components/distribucion/distribucion.component';
import { ProductoComponent } from './components/producto/producto.component';
import { ClientesProveedoresComponent } from './components/clientes-proveedores/clientes-proveedores.component';
import { ReportesComponent } from './components/reportes/reportes.component';
import { InicioComponent } from './components/inicio/inicio.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    VentasComponent,
    DistribucionComponent,
    ProductoComponent,
    ClientesProveedoresComponent,
    ReportesComponent,
    InicioComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
