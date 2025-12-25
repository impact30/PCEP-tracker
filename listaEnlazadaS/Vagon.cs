using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace listaEnlazadaS
{
    class Vagon
    {
        public int Dato { get; set; }
        public Vagon Sig { get; set; }

        public Vagon(int dato)
        {
            Dato = dato;
        }

        public Vagon() 
        { 
        
        }
    }
}
