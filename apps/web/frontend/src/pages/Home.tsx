import { useTranslation } from 'react-i18next';

const Home = () => {
  const { t } = useTranslation();

  const cipherCategories = [
    {
      id: "symmetric",
      title: t('home.categories.symmetric.title', { defaultValue: 'Symmetric Ciphers' }),
      description: t('home.categories.symmetric.description', { defaultValue: 'Secure data with shared secret keys' }),
      algorithms: ['vigenere', 'arc4', 'aes', 'chacha20'],
      icon: '🔐'
    },
    {
      id: "asymmetric",
      title: t('home.categories.asymmetric.title', { defaultValue: 'Asymmetric Ciphers' }),
      description: t('home.categories.asymmetric.description', { defaultValue: 'Public key cryptography for secure communication' }),
      algorithms: ['rsa', 'diffie-hellman', 'elgamal', 'ecc'],
      icon: '🔑'
    },
    {
      id: "prngs",
      title: t('home.categories.prngs.title', { defaultValue: 'PRNGs' }),
      description: t('home.categories.prngs.description', { defaultValue: 'Pseudorandom number generators' }),
      algorithms: ['prga', 'gpsL1Ca'],
      icon: '🎲'
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 to-slate-100">
      <section className="px-4 py-20 sm:px-6 lg:px-8 bg-purple-100">
        <div className="mx-auto max-w-4xl text-center">
          <h1 className="text-5xl font-bold tracking-tight text-slate-900 sm:text-6xl">
            {t('home.title', { defaultValue: 'Welcome to ' })}
            <span className="text-purple-800">{t('brand')}</span>
          </h1>
          <p className="mt-6 text-xl text-slate-600">
            {t('home.subtitle', { defaultValue: 'A modular Python framework for modern cryptography' })}
          </p>
          <p className="mt-4 text-lg text-slate-500">
            {t('home.description', { defaultValue: 'Explore cutting-edge encryption, hashing, key management, and secure data handling' })}
          </p>
          <div className="mt-8 flex justify-center gap-4">
            <button className="rounded-lg bg-purple-800 px-8 py-3 text-white hover:bg-purple-900 transition">
              {t('home.actions.getStarted', { defaultValue: 'Get Started' })}
            </button>
            <button className="rounded-lg border-2 border-purple-800 px-8 py-3 text-purple-800 hover:bg-purple-50 transition">
              {t('home.actions.learnMore', { defaultValue: 'Learn More' })}
            </button>
          </div>
        </div>
      </section>

      <section className="px-4 py-20 sm:px-6 lg:px-8 bg-white">
        <div className="mx-auto max-w-6xl">
          <h2 className="text-center text-4xl font-bold text-slate-900 mb-16">
            {t('home.coreCapabilities.title', { defaultValue: 'Core Capabilities' })}
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
                        {t(`sidebar.primitives.${algo}`, { defaultValue: algo })}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="px-4 py-20 sm:px-6 lg:px-8 bg-purple-100">
        <div className="mx-auto max-w-4xl">
          <h2 className="text-center text-4xl font-bold text-slate-900 mb-16">
            {t('home.why.title', { defaultValue: 'Why Choose Krypto?' })}
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="space-y-4">
              <div className="flex gap-4">
                <span className="text-3xl">📦</span>
                <div>
                  <h3 className="text-xl font-bold text-slate-900">{t('home.why.modular.title', { defaultValue: 'Modular Design' })}</h3>
                  <p className="text-slate-600">{t('home.why.modular.desc', { defaultValue: 'Independent modules for easy maintenance and expansion' })}</p>
                </div>
              </div>
              <div className="flex gap-4">
                <span className="text-3xl">🧪</span>
                <div>
                  <h3 className="text-xl font-bold text-slate-900">{t('home.why.tested.title', { defaultValue: 'Well-Tested' })}</h3>
                  <p className="text-slate-600">{t('home.why.tested.desc', { defaultValue: 'Comprehensive unit and integration tests included' })}</p>
                </div>
              </div>
            </div>
            <div className="space-y-4">
              <div className="flex gap-4">
                <span className="text-3xl">⚙️</span>
                <div>
                  <h3 className="text-xl font-bold text-slate-900">{t('home.why.extensible.title', { defaultValue: 'Extensible' })}</h3>
                  <p className="text-slate-600">{t('home.why.extensible.desc', { defaultValue: 'Easy to add new algorithms and features' })}</p>
                </div>
              </div>
              <div className="flex gap-4">
                <span className="text-3xl">🔒</span>
                <div>
                  <h3 className="text-xl font-bold text-slate-900">{t('home.why.secure.title', { defaultValue: 'Secure' })}</h3>
                  <p className="text-slate-600">{t('home.why.secure.desc', { defaultValue: 'Implements modern cryptographic standards' })}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="px-4 py-20 sm:px-6 lg:px-8 bg-purple-800">
        <div className="mx-auto max-w-4xl text-center">
          <h2 className="text-4xl font-bold text-white mb-6">
            {t('home.cta.title', { defaultValue: 'Start Exploring Cryptography Today' })}
          </h2>
          <p className="text-xl text-purple-100 mb-8">
            {t('home.cta.desc', { defaultValue: 'Access all cryptographic tools through an intuitive interface or command-line interface' })}
          </p>
          <button className="rounded-lg bg-white px-8 py-3 text-purple-800 font-semibold hover:bg-purple-50 transition">
            {t('home.cta.action', { defaultValue: 'Explore Algorithms' })}
          </button>
        </div>
      </section>
    </div>
  )
}

export default Home
