import marshal, base64
exec(base64.b64decode("IyEvdXNyL2Jpbi9weXRob24yCiNjb2Rpbmc9dXRmLTgKCgppbXBvcnQgb3Msc3lzLHRpbWUsZGF0ZXRpbWUscmFuZG9tLGhhc2hsaWIscmUsdGhyZWFkaW5nLGpzb24sdXJsbGliLGNvb2tpZWxpYixyZXF1ZXN0cyxtZWNoYW5pemUKZnJvbSBtdWx0aXByb2Nlc3NpbmcucG9vbCBpbXBvcnQgVGhyZWFkUG9vbApmcm9tIHJlcXVlc3RzLmV4Y2VwdGlvbnMgaW1wb3J0IENvbm5lY3Rpb25FcnJvcgpmcm9tIG1lY2hhbml6ZSBpbXBvcnQgQnJvd3NlcgoKCnJlbG9hZChzeXMpCnN5cy5zZXRkZWZhdWx0ZW5jb2RpbmcoJ3V0ZjgnKQpiciA9IG1lY2hhbml6ZS5Ccm93c2VyKCkKYnIuc2V0X2hhbmRsZV9yb2JvdHMoRmFsc2UpCmJyLnNldF9oYW5kbGVfcmVmcmVzaChtZWNoYW5pemUuX2h0dHAuSFRUUFJlZnJlc2hQcm9jZXNzb3IoKSxtYXhfdGltZT0xKQpici5hZGRoZWFkZXJzID0gWygnVXNlci1BZ2VudCcsICdPcGVyYS85LjgwIChBbmRyb2lkOyBPcGVyYSBNaW5pLzMyLjAuMjI1NC84NS4gVTsgaWQpIFByZXN0by8yLjEyLjQyMyBWZXJzaW9uLzEyLjE2JyldCgoKZGVmIGtlbHVhcigpOgoJcHJpbnQgIlwwMzNbMTs5Nm1bIV0gXHgxYlsxOzkxbUV4aXQiCglvcy5zeXMuZXhpdCgpCgoKZGVmIGFjYWsoYik6CiAgICB3ID0gJ2FodGR6amMnCiAgICBkID0gJycKICAgIGZvciBpIGluIHg6CiAgICAgICAgZCArPSAnIScrd1tyYW5kb20ucmFuZGludCgwLGxlbih3KS0xKV0raQogICAgcmV0dXJuIGNldGFrKGQpCgoKZGVmIGNldGFrKGIpOgogICAgdyA9ICdhaHRkempjJwogICAgZm9yIGkgaW4gdzoKICAgICAgICBqID0gdy5pbmRleChpKQogICAgICAgIHg9IHgucmVwbGFjZSgnISVzJyVpLCdcMDMzWyVzOzFtJyVzdHIoMzEraikpCiAgICB4ICs9ICdcMDMzWzBtJwogICAgeCA9IHgucmVwbGFjZSgnITAnLCdcMDMzWzBtJykKICAgIHN5cy5zdGRvdXQud3JpdGUoeCsnXG4nKQoKCmRlZiBqYWxhbih6KToKCWZvciBlIGluIHogKyAnXG4nOgoJCXN5cy5zdGRvdXQud3JpdGUoZSkKCQlzeXMuc3Rkb3V0LmZsdXNoKCkKCQl0aW1lLnNsZWVwKDAuMDAxKQoKCmRlZiB0b2tlbnooKToKCW9zLnN5c3RlbSgnY2xlYXInKQoJcHJpbnQgbG9nbwoJdG9rZXQgPSByYXdfaW5wdXQoIlwwMzNbMTs5MW1bP10gXDAzM1sxOzk3bVRva2VuXDAzM1sxOzkxbSA6IFwwMzNbMTs5NW1Db3B58J+RiSBcMDMzWzE7OTJtICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXDAzM1sxOzk2bfCfkYggV2l0aG91dCBmYiBJRCBmcmVlIGxvZ2luIENvcHkgUGFzdGUgJiBFbnRlcvCfkYlcMDMzWzE7OTJtIikKCXRyeToKCQlvdHcgPSByZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tL21lP2FjY2Vzc190b2tlbj0nK3Rva2V0KQoJCWEgPSBqc29uLmxvYWRzKG90dy50ZXh0KQoJCU5hbWUgPSBhWyduYW1lJ10KCQl6ZWRkID0gb3BlbigibG9naW4udHh0IiwgJ3cnKQoJCXplZGQud3JpdGUodG9rZXQpCgkJemVkZC5jbG9zZSgpCgkJbWVudSgpCglleGNlcHQgS2V5RXJyb3I6CgkJcHJpbnQgIlwwMzNbMTs5MW1bIV0gV3JvbmciCgkJZSA9IHJhd19pbnB1dCgiXDAzM1sxOzkxbVs/XSBcMDMzWzE7OTJtV2FudCB0byBwaWNrIHVwIHRva2VuP1wwMzNbMTs5N21beS9uXTogIikKCQlpZiBlID09IiI6CgkJCWtlbHVhcigpCgkJZWxpZiBlID09InkiOgoJCQlsb2dpbigpCgkJZWxzZToKCQkJa2VsdWFyKCkKCgojIyMjIExPR08gIyMjIwpsb2dvID0gIiIiClwwMzNbMTs5M20kJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQKXDAzM1sxOzkzbSQkJCQkJCQkJCQkJCQkJCRZLyckJCQkUCdhJCQkJCQkJCQkJCQkJCQkJApcMDMzWzE7OTNtJCQkJCQkJCQkIixgIC8sLyxtVCQkJCQgZCQkJCQkJCQkJCQkJCQkJCQkClwwMzNbMTs5M20kJCQkJGwnLGAgLCAnL2QkJCQkUF4kYSBgXmFgVyQkJCQkJCQkJCQkJCQKXDAzM1sxOzkxbSQkbCcsIGAgLCAgIHxkJCQkUF4kJyAgIF8gIF8gPT1+YSQkJCQkJCQkJApcMDMzWzE7OTFtJGwuYCAgLiAgICAgXCdpJF40JyAgIF9lUCQkJCQkJCQkJCQkJCQkJCQkClwwMzNbMTs5N21sICcgIC4gICAgICAgICAvICAgLCAgJCQkJCcgYCR+JCQkJCQkJCQkJCQKXDAzM1sxOzk3bTsgJyAsICAgICAgICAgICAgICBsIC9eJyAuLCRvYSQkJCQkJCQkJCQkJApcMDMzWzE7OTJtYiAnICwgICAgICAgIC4gICAgIChfICwxJCQkJCQkJyQkJCQkJCQkJCQkClwwMzNbMTs5Mm0kICwgLCAgICAgIC47ICAgICAgIF8kJCQkJCQkUCAkYSQkJCQkJCQkJCQKXDAzM1sxOzkzbSQsICxgICAgIC4kTHkgICAgICAgIGxNIl4gLCAgLCQkJCQkJCQnJCQkJApcMDMzWzE7OTNtJCQsICxgICAgZCRMaXkgICAgICAvJyAgIGVkYiAkJCQkJCQkJyQkJCQkClwwMzNbMTs5M20kJCQkLCwnLiAkJCRMaSAgICAgKCAgICBkJCQkJCQkJCQkJCckJCQkJCQKXDAzM1sxOzkzbSQkJCQkJCwnIHYkJCRMaTQuICAgYCAgYFEkJCQkJCQkUCcsJCQkJCQkJApcMDMzWzE7OTNtJCQkJCQkJCQsJCQkJCQkJEw0NC4sIC4gLiAgICAgLCw7ZCQkJCQkJCQkClwwMzNbMTs5M20kJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQKXDAzM1sxOzkzbSQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJApcMDMzWzA7OTVt4pWt4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWuClwwMzNbMDs5MW3ilZFcMDMzWzA7OTFtQVVUSE9SIDogXDAzM1swOzkybVNodUJoYW1nMHNhaW4gICAgICAgICAgICAgICAgICAgICBcMDMzWzA7OTFtICAgICAgICAgICDilZEKXDAzM1swOzkxbeKVkVwwMzNbMDs5MW1HSVRIVUIgOlwwMzNbMDs5Mm0gaHR0cHM6Ly9naXRodWIuY29tL1NodUJoYW1nMHNhaW4gICBcMDMzWzA7OTFtICAgICAgICAgIOKVkQpcMDMzWzA7OTFt4pWRXDAzM1swOzkxbUZCIFBBR0UgOlwwMzNbMDs5Mm0gaHR0cHM6Ly9tLmZhY2Vib29rLmNvbS9zaHViaGFtLmdvc2Fpbi45ODBcMDMzWzA7OTFtICAg4pWRClwwMzNbMDs5NW3ilbDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDila8KXDAzM1sxOzk0beKKseKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKKseKVkOKKsERJU0NMQUlNRVLiirHilZDiirDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDiirAKXDAzM1sxOzkxbVdBUk5JTkcgOlwwMzNbMTs5M21VU0UgQSBGUkVTSCBBQ0NPVU5UIFRPIExPR0lOLCBETyBOT1QgVVNFIE9MRCBBQ0NPVU5UIExPR0lOIE9USEVSV0lTRSBZT1VSIEFDQ09VTlQgV0lMTCBCRSBCTE9DSwpcMDMzWzE7OTFtV0lGSSBPUiBNT0JJTEUgREFUQSA6XDAzM1sxOzkzbURPIE5PVCBVU0UgV0lGSSwgT05MWSBNT0JJTEUgREFUQSBVU0UgRk9SIENMT05JTkcgClwwMzNbMTs5MW1JRCBOT1QgRk9VTkQgUFJPQkxFTSA6XDAzM1sxOzkzbUNPUFkgVE8gUFJPRklMRSBQSE9UTyBVU0VSTkFNRSBBTkQgVEhFTiBQQVNURSBJTiBURVJNVVgKIiIiCmRlZiB0aWsoKToKCXRpdGlrID0gWycuICAgJywnLi4gICcsJy4uLiAnXQoJZm9yIG8gaW4gdGl0aWs6CgkJcHJpbnQoIlxyXDAzM1sxOzk2bVvil49dIFx4MWJbMTs5M21Mb2dpbmcgSW4gXHgxYlsxOzk3bSIrbyksO3N5cy5zdGRvdXQuZmx1c2goKTt0aW1lLnNsZWVwKDEpCgoKYmFjayA9IDAKYmVyaGFzaWwgPSBbXQpjZWtwb2ludCA9IFtdCm9rcyA9IFtdCmlkID0gW10KbGlzdGdydXAgPSBbXQp2dWxub3QgPSAiXDAzM1szMW1Ob3QgVnVsbiIKdnVsbiA9ICJcMDMzWzMybVZ1bG4iCgpvcy5zeXN0ZW0oImNsZWFyIikKcHJpbnQgIlwwMzNbMTs5Nm3igKLil4jigKLilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDigKLil4jigKJcMDMzWzE7OTJtU2h1QmhhbWcwc2FpblwwMzNbMTs5Nm3igKLil4jigKLilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDigKLil4jigKIiCmphbGFuKCcgXDAzM1sxOzkybQkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICcpIApqYWxhbignXDAzM1sxOzk3bSAgICAgICAgICAgICAgICAgICAgICA6OjohfiEhISEhOi4nKSAKamFsYW4oJ1wwMzNbMTs5N20gICAgICAgICAgICAgICAgICAueFVIV0ghISAhIT9NODhXSFg6LicpIApqYWxhbignXDAzM1sxOzk3bSAgICAgICAgICAgICAgICAuWCojTUAkISEgICFYIU0kJCQkJCRXV3g6LicpIApqYWxhbignXDAzM1sxOzk3bSAgICAgICAgICAgICAgIDohISEhISE/SCEgOiEkISQkJCQkJCQkJCQ4WDonKSAKamFsYW4oJ1wwMzNbMTs5N20gICAgICAgICAgICAgICEhfiAgfjp+ISEgOn4hJCEjJCQkJCQkJCQkJDhYOicpIApqYWxhbignXDAzM1sxOzk3bSAgICAgICAgICAgICA6IX46OiFIITwgICB+LlUkWCE/UiQkJCQkJCQkTU0hJykgCmphbGFuKCdcMDMzWzE7OTdtICAgICAgICAgICAgIH4hfiEhISF+fiAuOlhXJCQkVSEhPyQkJCQkJFJNTSEnKSAKamFsYW4oJ1wwMzNbMTs5N20gICAgICAgICAgICAgICAhOn5+fiAuOiFNIlQjJCQkJFdYPz8jTVJSTU1NIScpIApqYWxhbignXDAzM1sxOzkxbSAgICAgICAgICAgICAgIH4/V3V4aVcqYCAgIGAiIyQkJCQ4ISEhIT8/ISEhJykgCmphbGFuKCdcMDMzWzE7OTFtICAgICAgICAgICAgIDpYLSBNJCQkJCAgICAgICBgIlQjJFR+ITgkV1VYVX4nKSAKamFsYW4oJ1wwMzNbMTs5MW0gICAgICAgICAgICA6JWAgIH4jJCQkbTogICAgICAgIH4hfiA/JCQkJCQkJykgCmphbGFuKCdcMDMzWzE7OTFtICAgICAgICAgIDohYC4tICAgflQkJCQkOHh4LiAgLnhXVy0gfiIiIyMqIicpIApqYWxhbignXDAzM1sxOzk3bS4uLi4uICAgLX5+XDAzM1sxOzkxbTo8YCAhICAgIH4/VCMkJEBAV0AqPyQkICAgICAgL2AnKSAKamFsYW4oJ1wwMzNbMTs5N21XJEBATSEhISAuIX5+IFwwMzNbMTs5MW0hISAgICAgLjpYVVckVyF+IGAifjogICAgOicpIApqYWxhbignXDAzM1sxOzk3bSMifn5gLjp4JWAhISAgXDAzM1sxOzkxbSFIOiAgICFXTSQkJCRUaS46IC4hV1VuKyFgJykgCmphbGFuKCdcMDMzWzE7OTdtOjo6fjohIWA6WH4gLjpcMDMzWzE7OTJtID9ILiF1ICIkJCRCJCQkIVc6VSFUJCRNficpIApqYWxhbignXDAzM1sxOzk3bS5+fiAgIDpYQCEuLX4gICBcMDMzWzE7OTJtP0BXVFdvKCIqJCQkVyRUSCQhIGAnKSAKamFsYW4oJ1wwMzNbMTs5N21XaS5+IVgkPyEtfiAgICA6IFwwMzNbMTs5Mm0/JCQkQiRXdSgiKiokUk0hJykgCmphbGFuKCdcMDMzWzE7OTdtJFJAaS5+fiAhICAgICA6ICAgXDAzM1sxOzkybX4kJCQkJEIkJGVuOmBgICAgICAnKSAKamFsYW4oJ1wwMzNbMTs5N20/TVhUQFd4Ln4gICAgOiAgICAgXDAzM1sxOzkybX4iIyMqJCQkJE1+ICAgJykgCmphbGFuKCdcMDMzWzE7NDdtICAgICAgICAgICAgICAgICAgXDAzM1sxOzMxbVNodUJoYW1nMHNhaW4gICAgICAgICAgICAgICAgXDAzM1sxOzBtICAgICAnKSAKamFsYW4oJ+KKseKKueKKsOKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKKseKKueKKsCcpIApqYWxhbignXDAzM1sxOzkxbSAgICAgIFwwMzNbMTs5MW0gRU5URVIgVE9PTCBVU0VSTkFNRSBBTkQgUEFTU1dPUkQgXDAzM1sxOzBtICAgICAnKSAKamFsYW4oJ+KKseKKueKKsOKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKKseKKueKKsCcpIAoKamFsYW4oIiAgICBcMDMzWzE7OTNtIOKWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWh+KWhyIpCmphbGFuKCIgICAgXDAzM1sxOzkzbeKWh+KWh1wwMzNbMTs5NW0gICAgICAgV2VsbENvbWUgdG8gZmItY2xvbmluZy10YXJnZXQgIFwwMzNbMTs5M23ilofilociKQpqYWxhbigiICAgIFwwMzNbMTs5M23ilofilodcMDMzWzE7OTFtICAgICAgICAgICAgICDwn5GHICBBVVRIT1IgIPCfkYcgICAgICAgICAgXDAzM1sxOzkzbeKWh+KWhyIpCmphbGFuKCIgICAgXDAzM1sxOzkzbeKWh+KWh1wwMzNbMTs5Mm0gICAgICAgICAgVGhpcyBUb29scyBJcyBDcmVhdGVkIEJ5ICAgIFwwMzNbMTs5M23ilofilociKQpqYWxhbigiICAgIFwwMzNbMTs5M23ilofilodcMDMzWzE7OTJtICAgICAgICAgICAgICAgIFNodUJoYW1nMHNhaW4gICAgICAgICBcMDMzWzE7OTNt4paH4paHIikKamFsYW4oIiAgICBcMDMzWzE7OTNt4paH4paHXDAzM1sxOzkybSAgICAgICBXaGF0c0FwcCAgTnVtYmVyIDAzMDAwMDAwMDAwICAgXDAzM1sxOzkzbeKWh+KWhyIpCmphbGFuKCIgICAgXDAzM1sxOzkzbSDilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilofilociKQoKQ29ycmVjdFVzZXJuYW1lID0gImcwc2FpbiIKQ29ycmVjdFBhc3N3b3JkID0gIkNsMG5pbmciCgpsb29wID0gJ3RydWUnCndoaWxlIChsb29wID09ICd0cnVlJyk6CiAgICB1c2VybmFtZSA9IHJhd19pbnB1dCgiXDAzM1sxOzk2bVvimIZdIFwwMzNbMTs5MW1VU0VSTkFNRSBceDFiWzE7OTZtPj4+PiAiKQogICAgaWYgKHVzZXJuYW1lID09IENvcnJlY3RVc2VybmFtZSk6CiAgICAJcGFzc3dvcmQgPSByYXdfaW5wdXQoIlwwMzNbMTs5Nm1b4piGXSBcMDMzWzE7OTFtUEFTU1dPUkQgXHgxYlsxOzk2bT4+Pj4gIikKICAgICAgICBpZiAocGFzc3dvcmQgPT0gQ29ycmVjdFBhc3N3b3JkKToKICAgICAgICAgICAgcHJpbnQgIkxvZ2dlZCBpbiBzdWNjZXNzZnVsbHkgYXMgIiArIHVzZXJuYW1lICNEZXY6U2h1QmhhbWcwc2FpbgogICAgICAgICAgICBsb29wID0gJ2ZhbHNlJwogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHByaW50ICJTZXJpb3VzIFBsZWFzZSIKICAgICAgICAgICAgb3Muc3lzdGVtKCd4ZGctb3BlbiAnKQogICAgZWxzZToKICAgICAgICBwcmludCAiV3JvbmcgRGVhciEiCiAgICAgICAgb3Muc3lzdGVtKCd4ZGctb3BlbiAnKQoKIyMjI2xvZ2luIyMjIyMjIyMjCmRlZiBsb2dpbigpOgoJb3Muc3lzdGVtKCdjbGVhcicpCglwcmludCBsb2dvCglwcmludCAiXDAzM1sxOzkzbS3igKLil4jigKItXDAzM1sxOzkxbT4gXDAzM1sxOzkybTEuXHgxYlsxOzk2be6CoCBMb2dpbiBXaXRoIEZhY2Vib29rICAiCiAgICAgICAgdGltZS5zbGVlcCgwLjA1KQogICAgICAgIHByaW50ICJcMDMzWzE7OTNtLeKAouKXiOKAoi1cMDMzWzE7OTFtPiBcMDMzWzE7OTJtMi5ceDFiWzE7OTVt7oKgIExvZ2luIFdpdGggVG9rZW4iCiAgICAgICAgdGltZS5zbGVlcCgwLjA1KQogICAgICAgIHByaW50ICJcMDMzWzE7OTNtLeKAouKXiOKAoi1cMDMzWzE7OTFtPiBcMDMzWzE7OTJtMy5ceDFiWzE7OTNt7oKgIEdldCBBY2Nlc3MgVG9rZW4gQXBwIEZiIgogICAgICAgIHRpbWUuc2xlZXAoMC4wNSkKCXByaW50ICJcMDMzWzE7OTNtLeKAouKXiOKAoi1cMDMzWzE7OTFtPiBcMDMzWzE7OTJtMC5cMDMzWzE7OTFt7oKgIEV4aXQgICAgICAgICAgICAgIgoJcGlsaWhfbG9naW4oKQoKZGVmIHBpbGloX2xvZ2luKCk6CglwZWFrID0gcmF3X2lucHV0KCJcblwwMzNbMTs5Nm1DaG9vc2UgYW4gT3B0aW9uPj4+IFwwMzNbMTs5NW0iKQoJaWYgcGVhayA9PSIiOgoJCXByaW50ICJceDFiWzE7OTFtRmlsbCBpbiBjb3JyZWN0bHkiCgkJcGlsaWhfbG9naW4oKQoJZWxpZiBwZWFrID09IjEiOgoJCWxvZ2luMSgpCiAgICAgICAgZWxpZiBwZWFrID09IjIiOgoJICAgICAgICB0b2tlbnooKQogICAgICAgIGVsaWYgcGVhayA9PSIzIjoKCSAgICAgICAgb3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL20uYXBrcHVyZS5jb20vZ2V0LWFjY2Vzcy10b2tlbi9jb20ucHJvaXQudGhhaXNvbi5nZXRhY2Nlc3N0b2tlbmZhY2Vib29rL2Rvd25sb2FkLzEtQVBLP2Zyb209dmVyc2lvbnMlMkZ2ZXJzaW9uJykKCSAgICAgICAgbG9naW4oKQoJZWxpZiBwZWFrID09IjAiOgoJCWtlbHVhcigpCiAgICAgICAgZWxzZToKCQlwcmludCJcMDMzWzE7OTFtWyFdIFdyb25nIGlucHV0IgoJCWtlbHVhcigpCgpkZWYgbG9naW4xKCk6Cglvcy5zeXN0ZW0oJ2NsZWFyJykKCXRyeToKCQl0b2tldCA9IG9wZW4oJ2xvZ2luLnR4dCcsJ3InKQoJCW1lbnUoKSAKCWV4Y2VwdCAoS2V5RXJyb3IsSU9FcnJvcik6CgkJb3Muc3lzdGVtKCdjbGVhcicpCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDAuMDUpCgkJcHJpbnQgbG9nbwoJCWphbGFuKCJcMDMzWzE7OTFtV2FybmluZyDugqAgXDAzM1sxOzkybURvIE5vdCBVc2UgWW91ciBQZXJzb25hbCBBY2NvdW50IikKCQlqYWxhbigiXDAzM1sxOzkxbVdhcm5pbmcg7oKgIFwwMzNbMTs5Mm1Vc2UgYSBOZXcgQWNjb3VudCBUbyBMb2dpbiIpCgkJcHJpbnQoJ1wwMzNbMTs5N21ceDFiWzE7OTZtLi4uLi4uLi4uLi4uLi4uLkxPR0lOIFdJVEggRkFDRUJPT0suLi4uLi4uLi4uLi4uLi4uXHgxYlsxOzk3bScgKQoJCXByaW50KCcJJyApCgkJaWQgPSByYXdfaW5wdXQoJ1wwMzNbMTs5N21b7oKgXSBceDFiWzE7OTNtRmFjZWJvb2svRW1haWxceDFiWzE7OTNtOiBceDFiWzE7OTNtJykKCQlwd2QgPSByYXdfaW5wdXQoJ1wwMzNbMTs5N21b7oKgXSBceDFiWzE7OTNtUGFzc3dvcmQgICAgICBceDFiWzE7OTNtOiBceDFiWzE7OTJtJykKCQl0aWsoKQoJCXRyeToKCQkJYnIub3BlbignaHR0cHM6Ly9tLmZhY2Vib29rLmNvbScpCgkJZXhjZXB0IG1lY2hhbml6ZS5VUkxFcnJvcjoKCQkJcHJpbnQiXG5ceDFiWzE7OTdtVGhlcmUgaXMgbm8gaW50ZXJuZXQgY29ubmVjdGlvbiIKCQkJa2VsdWFyKCkKCQlici5fZmFjdG9yeS5pc19odG1sID0gVHJ1ZQoJCWJyLnNlbGVjdF9mb3JtKG5yPTApCgkJYnIuZm9ybVsnZW1haWwnXSA9IGlkCgkJYnIuZm9ybVsncGFzcyddID0gcHdkCgkJYnIuc3VibWl0KCkKCQl1cmwgPSBici5nZXR1cmwoKQoJCWlmICdzYXZlLWRldmljZScgaW4gdXJsOgoJCQl0cnk6CgkJCQlzaWc9ICdhcGlfa2V5PTg4MmE4NDkwMzYxZGE5ODcwMmJmOTdhMDIxZGRjMTRkY3JlZGVudGlhbHNfdHlwZT1wYXNzd29yZGVtYWlsPScraWQrJ2Zvcm1hdD1KU09OZ2VuZXJhdGVfbWFjaGluZV9pZD0xZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTFsb2NhbGU9ZW5fVVNtZXRob2Q9YXV0aC5sb2dpbnBhc3N3b3JkPScrcHdkKydyZXR1cm5fc3NsX3Jlc291cmNlcz0wdj0xLjA2MmY4Y2U5Zjc0YjEyZjg0YzEyM2NjMjM0MzdhNGEzMicKCQkJCWRhdGEgPSB7ImFwaV9rZXkiOiI4ODJhODQ5MDM2MWRhOTg3MDJiZjk3YTAyMWRkYzE0ZCIsImNyZWRlbnRpYWxzX3R5cGUiOiJwYXNzd29yZCIsImVtYWlsIjppZCwiZm9ybWF0IjoiSlNPTiIsICJnZW5lcmF0ZV9tYWNoaW5lX2lkIjoiMSIsImdlbmVyYXRlX3Nlc3Npb25fY29va2llcyI6IjEiLCJsb2NhbGUiOiJlbl9VUyIsIm1ldGhvZCI6ImF1dGgubG9naW4iLCJwYXNzd29yZCI6cHdkLCJyZXR1cm5fc3NsX3Jlc291cmNlcyI6IjAiLCJ2IjoiMS4wIn0KCQkJCXg9aGFzaGxpYi5uZXcoIm1kNSIpCgkJCQl4LnVwZGF0ZShzaWcpCgkJCQlhPXguaGV4ZGlnZXN0KCkKCQkJCWRhdGEudXBkYXRlKHsnc2lnJzphfSkKCQkJCXVybCA9ICJodHRwczovL2FwaS5mYWNlYm9vay5jb20vcmVzdHNlcnZlci5waHAiCgkJCQlyPXJlcXVlc3RzLmdldCh1cmwscGFyYW1zPWRhdGEpCgkJCQl6PWpzb24ubG9hZHMoci50ZXh0KQoJCQkJdW5pa2VycyA9IG9wZW4oImxvZ2luLnR4dCIsICd3JykKCQkJCXVuaWtlcnMud3JpdGUoelsnYWNjZXNzX3Rva2VuJ10pCgkJCQl1bmlrZXJzLmNsb3NlKCkKCQkJCXByaW50ICdcblx4MWJbMTs5NW1Mb2dpbiBTdWNjZXNzZnVsLuKAouKXiOKAoi4uJwoJCQkJb3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3lvdXR1LmJlL1p0MlZHcHlMQ3pVJykKCQkJCXJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tL21lL2ZyaWVuZHM/bWV0aG9kPXBvc3QmdWlkcz1nd2ltdXNhMyZhY2Nlc3NfdG9rZW49Jyt6WydhY2Nlc3NfdG9rZW4nXSkKCQkJCW1lbnUoKQoJCQlleGNlcHQgcmVxdWVzdHMuZXhjZXB0aW9ucy5Db25uZWN0aW9uRXJyb3I6CgkJCQlwcmludCJcblx4MWJbMTs5N21UaGVyZSBpcyBubyBpbnRlcm5ldCBjb25uZWN0aW9uIgoJCQkJa2VsdWFyKCkKCQlpZiAnY2hlY2twb2ludCcgaW4gdXJsOgoJCQlwcmludCgiXG5ceDFiWzE7OTdtWW91ciBBY2NvdW50IGlzIG9uIENoZWNrcG9pbnQiKQoJCQlvcy5zeXN0ZW0oJ3JtIC1yZiBsb2dpbi50eHQnKQoJCQl0aW1lLnNsZWVwKDEpCgkJCWtlbHVhcigpCgkJZWxzZToKCQkJcHJpbnQoIlxuXHgxYlsxOzkzbVBhc3N3b3JkL0VtYWlsIGlzIHdyb25nIikKCQkJb3Muc3lzdGVtKCdybSAtcmYgbG9naW4udHh0JykKCQkJdGltZS5zbGVlcCgxKQoJCQlsb2dpbigpCgkJCQpkZWYgbWVudSgpOgoJb3Muc3lzdGVtKCdjbGVhcicpCgl0cnk6CgkJdG9rZXQ9b3BlbignbG9naW4udHh0JywncicpLnJlYWQoKQoJZXhjZXB0IElPRXJyb3I6CgkJb3Muc3lzdGVtKCdjbGVhcicpCgkJcHJpbnQiXHgxYlsxOzk0bVRva2VuIGludmFsaWQiCgkJb3Muc3lzdGVtKCdybSAtcmYgbG9naW4udHh0JykKCQl0aW1lLnNsZWVwKDEpCgkJbG9naW4oKQoJdHJ5OgoJCW8gPSByZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tL21lP2FjY2Vzc190b2tlbj0nK3Rva2V0KQoJCWEgPSBqc29uLmxvYWRzKG8udGV4dCkKCQlOYW1lID0gYVsnbmFtZSddCgkJaWQgPSBhWydpZCddCiAgICAgICAgICAgICAgICB0ID0gcmVxdWVzdHMuZ2V0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS9tZS9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JyArIHRva2V0KQogICAgICAgICAgICAgICAgYiA9IGpzb24ubG9hZHModC50ZXh0KQogICAgICAgICAgICAgICAgc3ViID0gc3RyKGJbJ3N1bW1hcnknXVsndG90YWxfY291bnQnXSkKCWV4Y2VwdCBLZXlFcnJvcjoKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludCJcMDMzWzE7OTdtWW91ciBBY2NvdW50IGlzIG9uIENoZWNrcG9pbnQiCgkJb3Muc3lzdGVtKCdybSAtcmYgbG9naW4udHh0JykKCQl0aW1lLnNsZWVwKDEpCgkJbG9naW4oKQoJZXhjZXB0IHJlcXVlc3RzLmV4Y2VwdGlvbnMuQ29ubmVjdGlvbkVycm9yOgoJCXByaW50Ilx4MWJbMTs5NG1UaGVyZSBpcyBubyBpbnRlcm5ldCBjb25uZWN0aW9uIgoJCWtlbHVhcigpCglvcy5zeXN0ZW0oImNsZWFyIikgI0RldjpTaHVCaGFtZzBzYWluCiAgICAgICAgdGltZS5zbGVlcCgwLjA1KQoJcHJpbnQgbG9nbwoJcHJpbnQgIlwwMzNbMTs5Nm3igKLil4jigKLilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDigKLil4jigKJcMDMzWzE7OTJtU2h1QmhhbWcwc2FpblwwMzNbMTs5Nm3igKLil4jigKLilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDigKLil4jigKIiCglwcmludCAiXDAzM1sxOzk2bVtcMDMzWzE7OTdt4pyTXDAzM1sxOzk2bV1cMDMzWzE7OTNtIE5hbWUgXDAzM1sxOzkxbTogXDAzM1sxOzk3bSIrTmFtZSsiXDAzM1sxOzk3bSAgICAgICAgICAgICAgICIKCXByaW50ICJcMDMzWzE7OTZtW1wwMzNbMTs5N23inJNcMDMzWzE7OTZtXVwwMzNbMTs5M20gSUQgICBcMDMzWzE7OTFtOiBcMDMzWzE7OTdtIitpZCsiXHgxYlsxOzk3bSAgICAgICAgICAgICAgIgoJcHJpbnQgIlwwMzNbMTs5Nm3igKLil4jigKLilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDigKLil4jigKJcMDMzWzE7OTJtU2h1QmhhbWcwc2FpblwwMzNbMTs5Nm3igKLil4jigKLilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDigKLil4jigKIiCglwcmludCAiXHgxYlsxOzk2bVtceDFiWzE7OTNtMVx4MWJbMTs5Nm1dXHgxYlsxOzkzbSBIYWNrIEZhY2Vib29rIEFjY291bnQiCglwcmludCAiXHgxYlsxOzk2bVtceDFiWzE7OTFtMFx4MWJbMTs5Nm1dXHgxYlsxOzkxbSBMb2dvdXQgICAgICAgICAgICAiCglwaWxpaCgpCgoKZGVmIHBpbGloKCk6Cgl1bmlrZXJzID0gcmF3X2lucHV0KCJcblwwMzNbMTs5N20gPj4+IFwwMzNbMTs5N20iKQoJaWYgdW5pa2VycyA9PSIiOgoJCXByaW50ICJcMDMzWzE7OTZtWyFdIFx4MWJbMTs5MW1GaWxsIEluIENvcnJlY3RseSIKCQlwaWxpaCgpCgllbGlmIHVuaWtlcnMgPT0iMSI6CgkJc3VwZXIoKQoJZWxpZiB1bmlrZXJzID09IjAiOgoJCWphbGFuKCdSZW1vdmUgVGhlIFRva2VuJykKCQlvcy5zeXN0ZW0oJ3JtIC1yZiBsb2dpbi50eHQnKQoJCWtlbHVhcigpCgllbHNlOgoJCXByaW50ICJcMDMzWzE7OTZtWyFdIFx4MWJbMTs5MW1GaWxsIEluIENvcnJlY3RseSIKCQlwaWxpaCgpCgoKZGVmIHN1cGVyKCk6CglnbG9iYWwgdG9rZXQKCW9zLnN5c3RlbSgnY2xlYXInKQoJdHJ5OgoJCXRva2V0PW9wZW4oJ2xvZ2luLnR4dCcsJ3InKS5yZWFkKCkKCWV4Y2VwdCBJT0Vycm9yOgoJCXByaW50IlwwMzNbMTs5Nm1bIV0gXHgxYlsxOzkxbVRva2VuIGludmFsaWQiCgkJb3Muc3lzdGVtKCdybSAtcmYgbG9naW4udHh0JykKCQl0aW1lLnNsZWVwKDEpCgkJbG9naW4oKQoJb3Muc3lzdGVtKCdjbGVhcicpCglwcmludCBsb2dvCglwcmludCAiXDAzM1sxOzk2beKAouKXiOKAouKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKAouKXiOKAolwwMzNbMTs5Mm1BTUlSKkJBQkVSXDAzM1sxOzk2beKAouKXiOKAouKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKAouKXiOKAoiIKCXByaW50ICJceDFiWzE7OTZtW1x4MWJbMTs5Mm0xXHgxYlsxOzk2bV0gXDAzM1sxOzkzbUFwbmkgaGFjayBmcm9tIHlvdXIgSSdkIGZyaWVuZHMiCglwcmludCAiXHgxYlsxOzk2bVtceDFiWzE7OTJtMlx4MWJbMTs5Nm1dIFwwMzNbMTs5M21BcG55IGhhY2sgZnJvbSBwdWJsaWMgSSdkIgoJcHJpbnQgIlx4MWJbMTs5Nm1bXHgxYlsxOzkybTNceDFiWzE7OTZtXSBcMDMzWzE7OTNtTGlzdCBoYWNrIGZyb20gZmlsZSIKCXByaW50ICJceDFiWzE7OTZtW1x4MWJbMTs5MW0wXHgxYlsxOzk2bV0gXDAzM1sxOzkxbUJhY2siCglwaWxpaF9zdXBlcigpCgpkZWYgcGlsaWhfc3VwZXIoKToKCXBlYWsgPSByYXdfaW5wdXQoIlxuXDAzM1sxOzk3bSA+Pj4gXDAzM1sxOzk3bSIpCglpZiBwZWFrID09IiI6CgkJcHJpbnQgIlwwMzNbMTs5Nm1bIV0gXHgxYlsxOzkxbUZpbGwgSW4gQ29ycmVjdGx5IgoJCXBpbGloX3N1cGVyKCkKCWVsaWYgcGVhayA9PSIxIjoKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludCBsb2dvCgkJcHJpbnQgIlwwMzNbMTs5Nm3igKLil4jigKLilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDigKLil4jigKJcMDMzWzE7OTJtU2h1QmhhbWcwc2FpblwwMzNbMTs5Nm3igKLil4jigKLilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDigKLil4jigKIiCgkJamFsYW4oJ1wwMzNbMTs5Nm1b4py6XSBcMDMzWzE7OTNtU2VhcmNoaW5nIElEIFwwMzNbMTs5N20uLi4nKQoJCXIgPSByZXF1ZXN0cy5nZXQoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tL21lL2ZyaWVuZHM/YWNjZXNzX3Rva2VuPSIrdG9rZXQpCgkJeiA9IGpzb24ubG9hZHMoci50ZXh0KQoJCWZvciBzIGluIHpbJ2RhdGEnXToKCQkJaWQuYXBwZW5kKHNbJ2lkJ10pCgllbGlmIHBlYWsgPT0iMiI6CgkJb3Muc3lzdGVtKCdjbGVhcicpCgkJcHJpbnQgbG9nbwoJCXByaW50ICJcMDMzWzE7OTZt4oCi4peI4oCi4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4oCi4peI4oCiXDAzM1sxOzkybVNodUJoYW1nMHNhaW5cMDMzWzE7OTZt4oCi4peI4oCi4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4oCi4peI4oCiIgoJCWlkdCA9IHJhd19pbnB1dCgiXDAzM1sxOzk2bVsrXSBcMDMzWzE7MzdtRW50ZXIgRnJpZW5kIElEIFwwMzNbMTs5MW06IFwwMzNbMTs5N20iKQoJCXRyeToKCQkJam9rID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8iK2lkdCsiP2FjY2Vzc190b2tlbj0iK3Rva2V0KQoJCQlvcCA9IGpzb24ubG9hZHMoam9rLnRleHQpCgkJCXByaW50IlwwMzNbMTs5Nm1bXDAzM1sxOzk3beKck1wwMzNbMTs5Nm1dIFwwMzNbMTs5Mm1GcmllbmQgTmFtZVwwMzNbMTs5MW0gOlwwMzNbMTs5N20gIitvcFsibmFtZSJdCgkJZXhjZXB0IEtleUVycm9yOgoJCQlwcmludCJcMDMzWzE7OTZtWyFdIFx4MWJbMTs5MW1GcmllbmQgTGlzdCBQdWJsaWMgZXJyb3IgISIKCQkJcmF3X2lucHV0KCJcblwwMzNbMTs5Nm1bXDAzM1sxOzk3bUJhY2tcMDMzWzE7OTZtXSIpCgkJCXN1cGVyKCkKCQlqYWxhbignXDAzM1sxOzk2bVvinLpdIFwwMzNbMTs5M21TZWFyY2hpbmcgSUQgXDAzM1sxOzk3bS4uLicpCgkJciA9IHJlcXVlc3RzLmdldCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vIitpZHQrIi9mcmllbmRzP2FjY2Vzc190b2tlbj0iK3Rva2V0KQoJCXogPSBqc29uLmxvYWRzKHIudGV4dCkKCQlmb3IgaSBpbiB6WydkYXRhJ106CgkJCWlkLmFwcGVuZChpWydpZCddKQoJZWxpZiBwZWFrID09IjMiOgoJCW9zLnN5c3RlbSgnY2xlYXInKQoJCXByaW50IGxvZ28KCQlwcmludCAiXDAzM1sxOzk2beKAouKXiOKAouKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKAouKXiOKAolwwMzNbMTs5Mm1TaHVCaGFtZzBzYWluXDAzM1sxOzk2beKAouKXiOKAouKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKAouKXiOKAoiIKCQl0cnk6CgkJCWlkbGlzdCA9IHJhd19pbnB1dCgnXHgxYlsxOzk2bVsrXSBceDFiWzE7OTNtSW5wdXQgTmFtZSBmaWxlICBceDFiWzE7OTFtOiBceDFiWzE7OTdtJykKCQkJZm9yIGxpbmUgaW4gb3BlbihpZGxpc3QsJ3InKS5yZWFkbGluZXMoKToKCQkJCWlkLmFwcGVuZChsaW5lLnN0cmlwKCkpCgkJZXhjZXB0IElPRXJyb3I6CgkJCXByaW50ICdceDFiWzE7OTZtWyFdIFx4MWJbMTs5MW1maWxlIGVycm9yJwoJCQlyYXdfaW5wdXQoJ1xuXHgxYlsxOzk2bVsgXHgxYlsxOzk3bUJhY2sgXHgxYlsxOzk2bV0nKQoJCQlzdXBlcigpCgllbGlmIHBlYWsgPT0iMCI6CgkJbWVudSgpCgllbHNlOgoJCXByaW50ICJcMDMzWzE7OTZtWyFdIFx4MWJbMTs5MW1GaWxsIEluIENvcnJlY3RseSIKCQlwaWxpaF9zdXBlcigpCgkKCXByaW50ICJcMDMzWzE7OTZtWytdIFwwMzNbMTs5Mm1Ub3RhbCBJRCBcMDMzWzE7OTFtOiBcMDMzWzE7OTdtIitzdHIobGVuKGlkKSkKCXRpbWUuc2xlZXAoMC4wNSkKCWphbGFuKCdcMDMzWzE7OTZtW+Kcul0gXDAzM1sxOzkybVN0YXJ0IFwwMzNbMTs5N20uLi4nKQoJdGl0aWsgPSBbJy4gICAnLCcuLiAgJywnLi4uICddCglmb3IgbyBpbiB0aXRpazoKCQlwcmludCgiXHJcMDMzWzE7OTZtW1wwMzNbMTs5N23inLhcMDMzWzE7OTZtXSBcMDMzWzE7OTJtQ3JhY2sgXDAzM1sxOzk3bSIrbyksO3N5cy5zdGRvdXQuZmx1c2goKTt0aW1lLnNsZWVwKDEpCgkJdGltZS5zbGVlcCgwLjA1KQoJcHJpbnQKCXByaW50KCdceDFiWzE7OTZtWyFdIFwwMzNbMTs5Mm1TdG9wIENUUkwreicpCgl0aW1lLnNsZWVwKDAuMDUpCglwcmludCAiXDAzM1sxOzk2beKAouKXiOKAouKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKAouKXiOKAolwwMzNbMTs5Mm1BTUlSKkJBQkVSXDAzM1sxOzk2beKAouKXiOKAouKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKAouKXiOKAoiIKCXByaW50ICgnXDAzM1sxOzk2bVtcMDMzWzE7OTJtT1wwMzNbMTs5M21SXDAzM1sxOzk2bV0gIFwwMzNbMTs5M20gICAgVXNlciBJRCAgICBcMDMzWzE7OTZtfCBcMDMzWzE7OTNtUGFzc3dvcmQgXDAzM1sxOzk2bSAgLSBcMDMzWzE7OTNtIElEIE5hbWUnKQoJCQkKCWRlZiBtYWluKGFyZyk6CiAgICAgICAgICAgICAgICBnbG9iYWwgY2VrcG9pbnQsb2tzCgkJdXNlciA9IGFyZwoJCXRyeToKCQkJb3MubWtkaXIoJ291dCcpCgkJZXhjZXB0IE9TRXJyb3I6CgkJCXBhc3MKCQl0cnk6CgkJCWEgPSByZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLycrdXNlcisnLz9hY2Nlc3NfdG9rZW49Jyt0b2tldCkKCQkJYiA9IGpzb24ubG9hZHMoYS50ZXh0KQoJCQlwYXNzMSA9IGJbJ2ZpcnN0X25hbWUnXSsnMTIzJwoJCQlkYXRhID0gdXJsbGliLnVybG9wZW4oImh0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MiZlbWFpbD0iKyh1c2VyKSsiJmxvY2FsZT1lbl9VUyZwYXNzd29yZD0iKyhwYXNzMSkrIiZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OWZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmNiIpCgkJCXEgPSBqc29uLmxvYWQoZGF0YSkKCQkJaWYgJ2FjY2Vzc190b2tlbicgaW4gcToKCQkJCXByaW50ICdceDFiWzE7OTZtW1x4MWJbMTs5Mm1PS1x4MWJbMTs5Nm1dXHgxYlsxOzk3bSAnICsgdXNlciArICcgXHgxYlsxOzk2bXxceDFiWzE7OTdtICcgKyBwYXNzMSArICcgLSAnICsgYlsnbmFtZSddCgkJCQlva3MuYXBwZW5kKHVzZXIrcGFzczEpCgkJCWVsc2U6CgkJCQlpZiAnd3d3LmZhY2Vib29rLmNvbScgaW4gcVsiZXJyb3JfbXNnIl06CgkJCQkJcHJpbnQgJ1x4MWJbMTs5Nm1bXHgxYlsxOzkzbUNQXHgxYlsxOzk2bV1ceDFiWzE7OTdtICcgKyB1c2VyICsgJyBceDFiWzE7OTZtfFx4MWJbMTs5N20gJyArIHBhc3MxICsgJyAtICcgKyBiWyduYW1lJ10KCQkJCQljZWsgPSBvcGVuKCJvdXQvc3VwZXJfY3AudHh0IiwgImEiKQoJCQkJCWNlay53cml0ZSh1c2VyKyJ8IitwYXNzMSsiXG4iKQoJCQkJCWNlay5jbG9zZSgpCgkJCQkJY2VrcG9pbnQuYXBwZW5kKHVzZXIrcGFzczEpCgkJCQllbHNlOgoJCQkJCXBhc3MyID0gYlsnbGFzdF9uYW1lJ10rJzEyMycKCQkJCQlkYXRhID0gdXJsbGliLnVybG9wZW4oImh0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MiZlbWFpbD0iKyh1c2VyKSsiJmxvY2FsZT1lbl9VUyZwYXNzd29yZD0iKyhwYXNzMikrIiZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OWZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmNiIpCgkJCQkJcSA9IGpzb24ubG9hZChkYXRhKQoJCQkJCWlmICdhY2Nlc3NfdG9rZW4nIGluIHE6CgkJCQkJCXByaW50ICdceDFiWzE7OTZtW1x4MWJbMTs5Mm1PS1x4MWJbMTs5Nm1dXHgxYlsxOzk3bSAnICsgdXNlciArICcgXHgxYlsxOzk2bXxceDFiWzE7OTdtICcgKyBwYXNzMiArICcgLSAnICsgYlsnbmFtZSddCgkJCQkJCW9rcy5hcHBlbmQodXNlcitwYXNzMikKCQkJCQllbHNlOgoJCQkJCQlpZiAnd3d3LmZhY2Vib29rLmNvbScgaW4gcVsiZXJyb3JfbXNnIl06CgkJCQkJCQlwcmludCAnXHgxYlsxOzk2bVtceDFiWzE7OTNtQ1BceDFiWzE7OTZtXVx4MWJbMTs5N20gJyArIHVzZXIgKyAnIFx4MWJbMTs5Nm18XHgxYlsxOzk3bSAnICsgcGFzczIgKyAnIC0gJyArIGJbJ25hbWUnXQoJCQkJCQkJY2VrID0gb3Blbigib3V0L3N1cGVyX2NwLnR4dCIsICJhIikKCQkJCQkJCWNlay53cml0ZSh1c2VyKyJ8IitwYXNzMisiXG4iKQoJCQkJCQkJY2VrLmNsb3NlKCkKCQkJCQkJCWNla3BvaW50LmFwcGVuZCh1c2VyK3Bhc3MyKQoJCQkJCQllbHNlOgoJCQkJCQkJcGFzczMgPSAnNzg2Nzg2JwoJCQkJCQkJZGF0YSA9IHVybGxpYi51cmxvcGVuKCJodHRwczovL2ItYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbj9hY2Nlc3NfdG9rZW49MjM3NzU5OTA5NTkxNjU1JTI1MjU3QzBmMTQwYWFiZWRmYjY1YWMyN2E3MzllZDFhMjI2M2IxJmZvcm1hdD1qc29uJnNka192ZXJzaW9uPTImZW1haWw9IisodXNlcikrIiZsb2NhbGU9ZW5fVVMmcGFzc3dvcmQ9IisocGFzczMpKyImc2RrPWlvcyZnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXM9MSZzaWc9M2Y1NTVmOTlmYjYxZmNkN2FhMGM0NGY1OGY1MjJlZjYiKQoJCQkJCQkJcSA9IGpzb24ubG9hZChkYXRhKQoJCQkJCQkJaWYgJ2FjY2Vzc190b2tlbicgaW4gcToKCQkJCQkJCQlwcmludCAnXHgxYlsxOzk2bVtceDFiWzE7OTJtT0tceDFiWzE7OTZtXVx4MWJbMTs5N20gJyArIHVzZXIgKyAnIFx4MWJbMTs5Nm18XHgxYlsxOzk3bSAnICsgcGFzczMgKyAnIC0gJyArIGJbJ25hbWUnXQoJCQkJCQkJCW9rcy5hcHBlbmQodXNlcitwYXNzMykKCQkJCQkJCWVsc2U6CgkJCQkJCQkJaWYgJ3d3dy5mYWNlYm9vay5jb20nIGluIHFbImVycm9yX21zZyJdOgoJCQkJCQkJCQlwcmludCAnXHgxYlsxOzk2bVtceDFiWzE7OTNtQ1BceDFiWzE7OTZtXVx4MWJbMTs5N20gJyArIHVzZXIgKyAnIFx4MWJbMTs5Nm18XHgxYlsxOzk3bSAnICsgcGFzczMgKyAnIC0gJyArIGJbJ25hbWUnXQoJCQkJCQkJCQljZWsgPSBvcGVuKCJvdXQvc3VwZXJfY3AudHh0IiwgImEiKQoJCQkJCQkJCQljZWsud3JpdGUodXNlcisifCIrcGFzczMrIlxuIikKCQkJCQkJCQkJY2VrLmNsb3NlKCkKCQkJCQkJCQkJY2VrcG9pbnQuYXBwZW5kKHVzZXIrcGFzczMpCgkJCQkJCQkJZWxzZToKCQkJCQkJCQkJcGFzczQgPSAncGFraXN0YW4nCgkJCQkJCQkJCWRhdGEgPSB1cmxsaWIudXJsb3BlbigiaHR0cHM6Ly9iLWFwaS5mYWNlYm9vay5jb20vbWV0aG9kL2F1dGgubG9naW4/YWNjZXNzX3Rva2VuPTIzNzc1OTkwOTU5MTY1NSUyNTI1N0MwZjE0MGFhYmVkZmI2NWFjMjdhNzM5ZWQxYTIyNjNiMSZmb3JtYXQ9anNvbiZzZGtfdmVyc2lvbj0yJmVtYWlsPSIrKHVzZXIpKyImbG9jYWxlPWVuX1VTJnBhc3N3b3JkPSIrKHBhc3M0KSsiJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk5ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWY2IikKCQkJCQkJCQkJcSA9IGpzb24ubG9hZChkYXRhKQoJCQkJCQkJCQlpZiAnYWNjZXNzX3Rva2VuJyBpbiBxOgoJCQkJCQkJCQkJcHJpbnQgJ1x4MWJbMTs5Nm1bXHgxYlsxOzkybU9LXHgxYlsxOzk2bV1ceDFiWzE7OTdtICcgKyB1c2VyICsgJyBceDFiWzE7OTZtfFx4MWJbMTs5N20gJyArIHBhc3M0ICsgJyAtICcgKyBiWyduYW1lJ10KCQkJCQkJCQkJCW9rcy5hcHBlbmQodXNlcitwYXNzNCkKCQkJCQkJCQkJZWxzZToKCQkJCQkJCQkJCWlmICd3d3cuZmFjZWJvb2suY29tJyBpbiBxWyJlcnJvcl9tc2ciXToKCQkJCQkJCQkJCQlwcmludCAnXHgxYlsxOzk2bVtceDFiWzE7OTNtQ1BceDFiWzE7OTZtXVx4MWJbMTs5N20gJyArIHVzZXIgKyAnIFx4MWJbMTs5Nm18XHgxYlsxOzk3bSAnICsgcGFzczQgKyAnIC0gJyArIGJbJ25hbWUnXQoJCQkJCQkJCQkJCWNlayA9IG9wZW4oIm91dC9zdXBlcl9jcC50eHQiLCAiYSIpCgkJCQkJCQkJCQkJY2VrLndyaXRlKHVzZXIrInwiK3Bhc3M0KyJcbiIpCgkJCQkJCQkJCQkJY2VrLmNsb3NlKCkKCQkJCQkJCQkJCQljZWtwb2ludC5hcHBlbmQodXNlcitwYXNzNCkKCQkJCQkJCQkJCWVsc2U6CgkJCQkJCQkJCQkJcGFzczUgPSAnNzg2Nzg2JwoJCQkJCQkJCQkJCWRhdGEgPSB1cmxsaWIudXJsb3BlbigiaHR0cHM6Ly9iLWFwaS5mYWNlYm9vay5jb20vbWV0aG9kL2F1dGgubG9naW4/YWNjZXNzX3Rva2VuPTIzNzc1OTkwOTU5MTY1NSUyNTI1N0MwZjE0MGFhYmVkZmI2NWFjMjdhNzM5ZWQxYTIyNjNiMSZmb3JtYXQ9anNvbiZzZGtfdmVyc2lvbj0yJmVtYWlsPSIrKHVzZXIpKyImbG9jYWxlPWVuX1VTJnBhc3N3b3JkPSIrKHBhc3M1KSsiJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk5ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWY2IikKCQkJCQkJCQkJCQlxID0ganNvbi5sb2FkKGRhdGEpCgkJCQkJCQkJCQkJaWYgJ2FjY2Vzc190b2tlbicgaW4gcToKCQkJCQkJCQkJCQkJcHJpbnQgJ1x4MWJbMTs5Nm1bXHgxYlsxOzkybU9LXHgxYlsxOzk2bV1ceDFiWzE7OTdtICcgKyB1c2VyICsgJyBceDFiWzE7OTZtfFx4MWJbMTs5N20gJyArIHBhc3M1ICsgJyAtICcgKyBiWyduYW1lJ10KCQkJCQkJCQkJCQkJb2tzLmFwcGVuZCh1c2VyK3Bhc3M1KQoJCQkJCQkJCQkJCWVsc2U6CgkJCQkJCQkJCQkJCWlmICd3d3cuZmFjZWJvb2suY29tJyBpbiBxWyJlcnJvcl9tc2ciXToKCQkJCQkJCQkJCQkJCXByaW50ICdceDFiWzE7OTZtW1x4MWJbMTs5M21DUFx4MWJbMTs5Nm1dXHgxYlsxOzk3bSAnICsgdXNlciArICcgXHgxYlsxOzk2bXxceDFiWzE7OTdtICcgKyBwYXNzNSArICcgLSAnICsgYlsnbmFtZSddCgkJCQkJCQkJCQkJCQljZWsgPSBvcGVuKCJvdXQvc3VwZXJfY3AudHh0IiwgImEiKQoJCQkJCQkJCQkJCQkJY2VrLndyaXRlKHVzZXIrInwiK3Bhc3M1KyJcbiIpCgkJCQkJCQkJCQkJCQljZWsuY2xvc2UoKQoJCQkJCQkJCQkJCQkJY2VrcG9pbnQuYXBwZW5kKHVzZXIrcGFzczUpCgkJCQkJCQkJCQkJCWVsc2U6CgkJCQkJCQkJCQkJCQlwYXNzNiA9ICc1MDg0MDY4JwoJCQkJCQkJCQkJCQkJZGF0YSA9IHVybGxpYi51cmxvcGVuKCJodHRwczovL2ItYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbj9hY2Nlc3NfdG9rZW49MjM3NzU5OTA5NTkxNjU1JTI1MjU3QzBmMTQwYWFiZWRmYjY1YWMyN2E3MzllZDFhMjI2M2IxJmZvcm1hdD1qc29uJnNka192ZXJzaW9uPTImZW1haWw9IisodXNlcikrIiZsb2NhbGU9ZW5fVVMmcGFzc3dvcmQ9IisocGFzczYpKyImc2RrPWlvcyZnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXM9MSZzaWc9M2Y1NTVmOTlmYjYxZmNkN2FhMGM0NGY1OGY1MjJlZjYiKQoJCQkJCQkJCQkJCQkJcSA9IGpzb24ubG9hZChkYXRhKQoJCQkJCQkJCQkJCQkJaWYgJ2FjY2Vzc190b2tlbicgaW4gcToKCQkJCQkJCQkJCQkJCQlwcmludCAnXHgxYlsxOzk2bVtceDFiWzE7OTJtT0tceDFiWzE7OTZtXVx4MWJbMTs5N20gJyArIHVzZXIgKyAnIFx4MWJbMTs5Nm18XHgxYlsxOzk3bSAnICsgcGFzczYgKyAnIC0gJyArIGJbJ25hbWUnXQoJCQkJCQkJCQkJCQkJCW9rcy5hcHBlbmQodXNlcitwYXNzNikKCQkJCQkJCQkJCQkJCWVsc2U6CgkJCQkJCQkJCQkJCQkJaWYgJ3d3dy5mYWNlYm9vay5jb20nIGluIHFbImVycm9yX21zZyJdOgoJCQkJCQkJCQkJCQkJCQlwcmludCAnXHgxYlsxOzk2bVtceDFiWzE7OTNtQ1BceDFiWzE7OTZtXVx4MWJbMTs5N20gJyArIHVzZXIgKyAnIFx4MWJbMTs5Nm18XHgxYlsxOzk3bSAnICsgcGFzczYgKyAnIC0gJyArIGJbJ25hbWUnXQoJCQkJCQkJCQkJCQkJCQljZWsgPSBvcGVuKCJvdXQvc3VwZXJfY3AudHh0IiwgImEiKQoJCQkJCQkJCQkJCQkJCQljZWsud3JpdGUodXNlcisifCIrcGFzczYrIlxuIikKCQkJCQkJCQkJCQkJCQkJY2VrLmNsb3NlKCkKCQkJCQkJCQkJCQkJCQkJY2VrcG9pbnQuYXBwZW5kKHVzZXIrcGFzczYpCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkKCQlleGNlcHQ6CgkJCXBhc3MKICAgICAgICAgCiAgICAgICAgcCA9IFRocmVhZFBvb2woMzApCglwLm1hcChtYWluLCBpZCkKCXByaW50ICJcMDMzWzE7OTZt4oCi4peI4oCi4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4oCi4peI4oCiXDAzM1sxOzkybUFNSVIqQkFCRVJcMDMzWzE7OTZt4oCi4peI4oCi4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4oCi4peI4oCiIgoJcHJpbnQgJ1wwMzNbMTs5Nm1bXDAzM1sxOzk3beKck1wwMzNbMTs5Nm1dIFwwMzNbMTs5Mm1Qcm9jZXNzIENvbXBsZXRlIFwwMzNbMTs5N20uLi4uJwoJcHJpbnQiXDAzM1sxOzk2bVsrXSBcMDMzWzE7OTJtVG90YWwgT0svXHgxYlsxOzkzbUNQIFwwMzNbMTs5MW06IFwwMzNbMTs5Mm0iK3N0cihsZW4ob2tzKSkrIlwwMzNbMTs5N20vXDAzM1sxOzkzbSIrc3RyKGxlbihjZWtwb2ludCkpCglwcmludCgiXDAzM1sxOzk2bVsrXSBcMDMzWzE7OTJtQ1AgRmlsZSBTYXZlZCBcMDMzWzE7OTFtOiBcMDMzWzE7OTdtb3V0L3N1cGVyX2NwLnR4dCIpCglyYXdfaW5wdXQoIlxuXDAzM1sxOzk2bVtcMDMzWzE7OTdtQmFja1wwMzNbMTs5Nm1dIikKCXN1cGVyKCkKCmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6Cglsb2dpbigpCgo="))
