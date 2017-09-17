# CONSTANTS   BEGIN
# # ALIGNMENTS
POSITIVE            = 'positive'
NEGATIVE            = 'negative'
# # CATEGORIES
METAGENETIC         = 'metagenetic'
# # SOURCES
RC                  = 'runnerscompanion'
# CONSTANTS   END

# CLASS       BEGIN
class Quality():
    def __init__(self,name,alignment,category,cost,source):
        """Quality(name,alignment,category,cost,source)"""
        # name is a string
        self.name       = name
        # alignment of quality
        self.alignment  = alignment
        # category of quality
        self.category   = category
        # cost in BP
        self.cost       = cost
        # tuple with (Book,Page)
        self.source     = source
        qualities.append(self)
        pass
# CLASS       END

# LIST        BEGIN
qualities           = []
# LIST        END

# QUALITIES   BEGIN

lowlightvision      = Quality('Low-Light Vision',     \
                              POSITIVE,METAGENETIC,5, \
                              (RC,114)                \
                             )
thermographicvision = Quality('Thermographic Vision', \
                              POSITIVE,METAGENETIC,5, \
                              (RC,115)                \
                             )

# QUALITIES   END