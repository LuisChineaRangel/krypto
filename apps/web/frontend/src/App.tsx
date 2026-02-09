
import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import Home from "./pages/Home";
import AESPage from "./pages/primitives/AES";
import VigenerePage from "./pages/primitives/Vigenere";
import ARC4Page from "./pages/primitives/ARC4";
import ChaCha20Page from "./pages/primitives/ChaCha20";
import RSAPage from "./pages/primitives/RSA";
import ECCPage from "./pages/primitives/ECC";
import ECDHPage from "./pages/primitives/ECDH";
import ECEGPage from "./pages/primitives/ECEG";
import DiffieHellmanPage from "./pages/primitives/DiffieHellman";
import ElGamalPage from "./pages/primitives/ElGamal";
import GPSL1CAPage from "./pages/primitives/GPSL1CA";
import PRGAPage from "./pages/primitives/PRGA";

const App = () => (
    <BrowserRouter>
        <MainLayout>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/aes" element={<AESPage />} />
                <Route path="/vigenere" element={<VigenerePage />} />
                <Route path="/arc4" element={<ARC4Page />} />
                <Route path="/chacha20" element={<ChaCha20Page />} />
                <Route path="/rsa" element={<RSAPage />} />
                <Route path="/ecc" element={<ECCPage />} />
                <Route path="/ecdh" element={<ECDHPage />} />
                <Route path="/eceg" element={<ECEGPage />} />
                <Route path="/diffie-hellman" element={<DiffieHellmanPage />} />
                <Route path="/elgamal" element={<ElGamalPage />} />
                <Route path="/gps-l1-ca" element={<GPSL1CAPage />} />
                <Route path="/prga" element={<PRGAPage />} />
            </Routes>
        </MainLayout>
    </BrowserRouter>
);

export default App;
