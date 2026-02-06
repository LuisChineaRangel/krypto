
import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import Home from "./pages/Home";
import AESPage from "./pages/AES";
import VigenerePage from "./pages/Vigenere";
import ARC4Page from "./pages/ARC4";
import ChaCha20Page from "./pages/ChaCha20";
import RSAPage from "./pages/RSA";
import ECCPage from "./pages/ECC";
import ECDHPage from "./pages/ECDH";
import ECEGPage from "./pages/ECEG";
import DiffieHellmanPage from "./pages/DiffieHellman";
import ElGamalPage from "./pages/ElGamal";
import GPSL1CAPage from "./pages/GPSL1CA";
import PRGAPage from "./pages/PRGA";

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
