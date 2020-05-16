class req_h:

    def __init__(self, sources, category, q, language, country, pageSize):
        self.sources = sources
        self.category = category
        self.q = q
        self.language = language
        self.country = country
        self.pageSize = pageSize

class req_e:
    def __init__(self, q , sources, domains, category,  language, country, to, sortBy, pageSize):
        self.q = q
        self.sources = sources
        self.domains = domains
        self.category = category
        self.language = language
        self.country = country
        self.to = to
        self.sortBy = sortBy
        self.pageSize = pageSize

