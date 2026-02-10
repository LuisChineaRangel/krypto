
import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainLayout from "@layouts/MainLayout";

import Home from "@pages/Home";
import NotFound from "@pages/NotFound";
import PrimitivePage from "@pages/primitives/PrimitivePage";

const App = () => (
    <BrowserRouter>
        <MainLayout>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/aes" element={<PrimitivePage id="aes" />} />
                <Route path="/vigenere" element={<PrimitivePage id="vigenere" />} />
                <Route path="/arc4" element={<PrimitivePage id="arc4" />} />
                <Route path="/chacha20" element={<PrimitivePage id="chacha20" />} />
                <Route path="/rsa" element={<PrimitivePage id="rsa" />} />
                <Route path="/ecc" element={<PrimitivePage id="ecc" />} />
                <Route path="/ecdh" element={<PrimitivePage id="ecdh" />} />
                <Route path="/eceg" element={<PrimitivePage id="eceg" />} />
                <Route path="/diffie-hellman" element={<PrimitivePage id="diffie-hellman" />} />
                <Route path="/elgamal" element={<PrimitivePage id="elgamal" />} />
                <Route path="/gps-l1-ca" element={<PrimitivePage id="gps-l1-ca" />} />
                <Route path="/prga" element={<PrimitivePage id="prga" />} />
                <Route path="/404" element={<NotFound />} />
                <Route path="*" element={<NotFound />} />
            </Routes>
        </MainLayout>
    </BrowserRouter>
);

export default App;
