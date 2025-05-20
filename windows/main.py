import ui_clienteAgregar
import ui_clienteBorrar
import ui_clienteModificar
import ui_clientes
import ui_clienteVentas
import ui_clienteVentasBorrar
import ui_inicio

import ui_menu
import ui_productoAgregar
import ui_productoBorrar
import ui_productoModificar
import ui_productos
import ui_productosVariacion
import ui_productoVariacionAgregar
import ui_productoVariacionBorrar
import ui_productoVariacionModificar
import ui_proveedorAgregar
import ui_proveedorBorrar
import ui_proveedores
import ui_proveedorModificar
import ui_proveedorProducto
import ui_proveedorProductoAgregar
import ui_proveedorProductoBorrar
import ui_proveedorProductoModificar
import ui_venta
import ui_ventasBuscar
import ui_ventasError
import db
import sys
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ui_inicio.inicio()
    window.show()
    sys.exit(app.exec())