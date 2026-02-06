const Home = () => {
  const cipherCategories = [
    {
      id: "symmetric",
      title: "Symmetric Ciphers",
      description: "Secure data with shared secret keys",
      algorithms: ["Vigenère", "RC4 (ARC4)", "AES", "ChaCha20"],
      icon: "🔐"
    },
    {
      id: "asymmetric",
      title: "Asymmetric Ciphers",
      description: "Public key cryptography for secure communication",
      algorithms: ["RSA", "Diffie-Hellman", "ElGamal", "ECC"],
      icon: "🔑"
    },
    {
      id: "prngs",
      title: "PRNGs",
      description: "Pseudorandom number generators",
      algorithms: ["PRGA (ARC4)", "GPS L1 C/A"],
      icon: "🎲"
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 to-slate-100">
      <section className="px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-4xl text-center">
          <h1 className="text-5xl font-bold tracking-tight text-slate-900 sm:text-6xl">
            Welcome to <span className="text-purple-800">Krypto</span>
          </h1>
          <p className="mt-6 text-xl text-slate-600">
            A modular Python framework for modern cryptography
          </p>
          <p className="mt-4 text-lg text-slate-500">
            Explore cutting-edge encryption, hashing, key management, and secure data handling
          </p>
          <div className="mt-8 flex justify-center gap-4">
            <button className="rounded-lg bg-purple-800 px-8 py-3 text-white hover:bg-purple-900 transition">
              Get Started
            </button>
            <button className="rounded-lg border-2 border-purple-800 px-8 py-3 text-purple-800 hover:bg-purple-50 transition">
              Learn More
            </button>
          </div>
        </div>
      </section>

      <section className="px-4 py-20 sm:px-6 lg:px-8 bg-white">
        <div className="mx-auto max-w-6xl">
          <h2 className="text-center text-4xl font-bold text-slate-900 mb-16">
            Core Capabilities
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {cipherCategories.map((category) => (
              <div key={category.id} className="rounded-xl border-2 border-slate-200 p-8 hover:shadow-lg transition">
                <div className="text-5xl mb-4">{category.icon}</div>
                <h3 className="text-2xl font-bold text-slate-900 mb-2">
                  {category.title}
                </h3>
                <p className="text-slate-600 mb-6">
                  {category.description}
                </p>
                <ul className="space-y-2">
                  {category.algorithms.map((algo) => (
                    <li key={algo} className="flex items-center text-slate-700">
                      <span className="mr-2 text-blue-600">✓</span>
                      {algo}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-4xl">
          <h2 className="text-center text-4xl font-bold text-slate-900 mb-16">
            Why Choose Krypto?
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="space-y-4">
              <div className="flex gap-4">
                <span className="text-3xl">📦</span>
                <div>
                  <h3 className="text-xl font-bold text-slate-900">Modular Design</h3>
                  <p className="text-slate-600">Independent modules for easy maintenance and expansion</p>
                </div>
              </div>
              <div className="flex gap-4">
                <span className="text-3xl">🧪</span>
                <div>
                  <h3 className="text-xl font-bold text-slate-900">Well-Tested</h3>
                  <p className="text-slate-600">Comprehensive unit and integration tests included</p>
                </div>
              </div>
            </div>
            <div className="space-y-4">
              <div className="flex gap-4">
                <span className="text-3xl">⚙️</span>
                <div>
                  <h3 className="text-xl font-bold text-slate-900">Extensible</h3>
                  <p className="text-slate-600">Easy to add new algorithms and features</p>
                </div>
              </div>
              <div className="flex gap-4">
                <span className="text-3xl">🔒</span>
                <div>
                  <h3 className="text-xl font-bold text-slate-900">Secure</h3>
                  <p className="text-slate-600">Implements modern cryptographic standards</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="px-4 py-20 sm:px-6 lg:px-8 bg-purple-800">
        <div className="mx-auto max-w-4xl text-center">
          <h2 className="text-4xl font-bold text-white mb-6">
            Start Exploring Cryptography Today
          </h2>
          <p className="text-xl text-purple-100 mb-8">
            Access all cryptographic tools through an intuitive interface or command-line interface
          </p>
          <button className="rounded-lg bg-white px-8 py-3 text-purple-800 font-semibold hover:bg-purple-50 transition">
            Explore Algorithms
          </button>
        </div>
      </section>
    </div>
  )
}

export default Home
