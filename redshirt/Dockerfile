FROM centos:7

RUN \
  yum -y install epel-release && \
  yum -y install supervisor

#FROM centos-supervisor

COPY mgr.sh /
COPY serviceA.sh /
COPY serviceB.sh /
COPY bootstrap.sh /
COPY supervisord.conf /

RUN mkdir /supervisord

CMD /bootstrap.sh
